from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, StudentSignUpForm, StudentUpdateForm
from .forms import UserUpdateForm,StudentSignUpForm, StudentUpdateForm, TeacherSignUpForm,TeacherUpdateForm, ReportForm,Users_Report_Form
from . import forms
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Student,Teacher,Report,Users_Report
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader

from django.contrib.auth import update_session_auth_hash
# Create your views here.

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'home',{'form': form})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

# ===============================Student ===========================
def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(user= user)
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='studentg')
            user.groups.add(group)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_register.html', {'form': form})

@login_required
def student_profile(request,username):
    user1 = User.objects.get(username=username)
    context = {
        'user1': user1,
    }
    return render(request, 'accounts/student_profile.html', context)

@login_required
@allowed_users(allowed_roles = ['studentg','admin'])
def edit_student(request):

    if request.method == 'POST':
        su_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if su_form.is_valid() and sp_form.is_valid():
            su_form.save()
            sp_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        su_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'su_form': su_form,
        'sp_form': sp_form,
        'user1': request.user,
        }
    return render(request, 'accounts/edit_student.html', context)

# ===============================Teacher ===========================
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            teacher = Teacher.objects.create(user = user)
            # teacher.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='teacherg')
            user.groups.add(group)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = TeacherSignUpForm()
    return render(request, 'accounts/teacher_register.html', {'form': form})



@login_required
def teacher_profile(request,username):

    user1 = User.objects.get(username=username)
# ========================================================================
    # s_id = request.user.id
    # lst_teachers = Student.objects.get(user_id = s_id).Followed_On


    ss = Report.objects.order_by('teacher_id')
    report_lst = []
    report_st = []
    report_st2 = []
    print(ss)
    for i in ss:
        print('type = ',type(Student.objects.get(user = i.user)))
        # print((type(i.user)))
        if(str(i.teacher) == user1.username):
            report_lst.append(i)
            report_st.append(Student.objects.get(user = i.user))
            report_st2.append(Student.objects.get(user = i.user).user.username)

# =======================================================================

    if request.user.groups.filter(name='studentg').exists():
        if request.method == 'POST':
            t_id = User.objects.get(username=username).id
            t = Teacher.objects.get(user_id = t_id)
            lst_students = t.followed_by
            s_id = request.user.id
            lst_teachers = Student.objects.get(user_id = s_id).Followed_On
            s = request.user

            if request.user.groups.filter(name='studentg').exists():
                lst_students.add(s)
                lst_teachers.add(t)

            lst_s = Student.objects.get(user_id = s_id).get_following() #list of teachers that the student is followed
            lst_t = Teacher.objects.get(user_id = t_id).get_followed_by() #list of students that follow on teacher
            return render(request, 'accounts/teacher_profile.html' , {'user1': user1 , 'lst_s' : lst_s, 'lst_t': lst_t})


    context = {
            'user1': user1 , 'lst_t': Teacher.objects.get(user_id = User.objects.get(username=username).id).get_followed_by()
             }
    if len(report_lst) != 0:
        context['report_lst'] =  report_lst
    if len(report_st) != 0:
        context['report_st'] = report_st
    if len(report_st2) != 0:
        context['report_st2'] = report_st2
    print(context)
    return render(request, 'accounts/teacher_profile.html', context)



@login_required
@allowed_users(allowed_roles = ['teacherg','admin'])
def edit_teacher(request):

    if request.method == 'POST':
        tu_form = UserUpdateForm(request.POST, instance=request.user)
        tp_form = TeacherUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.teacher)
        if tu_form.is_valid() and tp_form.is_valid():
            tu_form.save()
            tp_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')
    else:
        tu_form = UserUpdateForm(instance=request.user)
        tp_form = TeacherUpdateForm(instance=request.user.teacher)

    context = {
        'tu_form': tu_form,
        'tp_form': tp_form,
        }
    return render(request, 'accounts/edit_teacher.html', context)

def profile(request,username):
    if request.user.groups.filter(name='teacherg').exists():
        return HttpResponse(teacher_profile(request, username))
    else:
        return HttpResponse(student_profile(request, username))


#=========================================================
@login_required
def report(request, username):
    teacher = User.objects.get(username=username)
    user = request.user

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user


            rate.teacher = teacher.teacher
            rate.save()
            # else:
            #
            #     print("sdsd   ",rate.user.student)
            #     print("aaaa=======aaaa ",teacher.student)
            #     rate.user.student = teacher.student
            #     rate.save()
            return redirect('home')

    else:
    	form = ReportForm()

    template = loader.get_template('accounts/report.html')

    context = {
    	'form': form,
    	'teacher': teacher,
    }

    return HttpResponse(template.render(context, request))


def teacher_lst(request):
    teachers = Teacher.objects.order_by('user')
    context = { 'teachers': teachers }
    return render(request, 'accounts/teacher_list.html', context)

def student_lst(request):
    students = Student.objects.order_by('user')
    context = { 'students': students }
    return render(request, 'accounts/student_list.html', context)


def police(request):
    if request.method == 'POST':
        form = Users_Report_Form(request.POST)
        f_user = request.user

        if form.is_valid():
            user = form.save()
            user.from_police = f_user
            user.save()
            messages.success(request, f'Your Report Was Sent To The Administrator!')
            return redirect('home')
    else:
        form = Users_Report_Form()
    return render(request, 'accounts/police.html', {'form': form})
