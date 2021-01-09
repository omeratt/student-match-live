# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User, AbstractUser
# from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile,Student
from .models import Student, Teacher, RATE_CHOICES, Report,Users_Report
from django.db import transaction


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = False)
    username = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':1}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']


# ==============================================Student =================================
class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField()
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        # Student.is_student = True
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class StudentUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)

    class Meta:
        model = Student
        fields = ['Profile_pic','cv','study_choice','years_in_academy','Gender']

# ==============================================Teacher =================================

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField()
    # profile_Pic = forms.ImageField(required = False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']



class TeacherUpdateForm(forms.ModelForm):
    cv = forms.FileField(required = False,label = 'CV')
    Profile_pic = forms.ImageField(required = False)
    class Meta:
        model = Teacher
        fields = ['undergraduate','description','Profile_pic','cv','Gender']

#=============================================================================
class ReportForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=False)

	class Meta:
		model = Report
		fields = ['text', 'rate']

class Users_Report_Form(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)

	class Meta:
		model = Users_Report
		fields = ['text', 'on_user']
