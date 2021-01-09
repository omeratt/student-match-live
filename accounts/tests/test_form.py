from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from django.contrib.auth.forms import UserCreationForm
from .. import forms

class TestForms(SimpleTestCase,UserCreationForm):

    def test_student_sign_form_valid(self):
        form = forms.StudentSignUpForm(data={
            'first_name': 'ss',
            'last_name': 'ss',
            'password1':'asdasd123123',
            'username': 'ggg',
            'email': 'sdf@s.com','password2':'asdasd123123',
            })
        self.assertTrue(form.is_valid())


    def test_student(self):
        form = forms.StudentUpdateForm(data={
            'Profile_pic': 'ss',
            'cv': 'ss',
            'study_choice':'aerospace engineering',
            'years_in_academy': 'Freshman',
            'Gender': 'male',
            })
        self.assertTrue(form.is_valid())

    def test_teacher_sign_form_valid(self):
        form = forms.TeacherSignUpForm(data={
            'first_name': 'ss',
            'last_name': 'ss',
            'password1':'asdasd123123',
            'username': 'ggg',
            'email': 'sdf@s.com','password2':'asdasd123123',
            })
        self.assertTrue(form.is_valid())

    def test_teacher(self):
        form = forms.TeacherUpdateForm(data={
            'Profile_pic': 'ss',
            'cv': 'ss',
            'undergraduate':'BA',
            'description': 'sdf',
            'Gender': 'male',
            })
        self.assertTrue(form.is_valid())

    def test_report(self):
        form = forms.ReportForm(data={
            'text': 'ss',
            'rate': 1,
            })
        self.assertTrue(form.is_valid())

    def test_user_report(self):
        form = forms.Users_Report_Form(data={
            'text': 'ssss',
            'on_user':'fff',
            'from_police':'d',
            })
        self.assertFalse(form.is_valid())
