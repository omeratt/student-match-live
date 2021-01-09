from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from accounts.views import student_register,edit_student,student_profile,teacher_register,teacher_profile,edit_teacher

class TestUrls(SimpleTestCase):


    def test_student_register_url_is_resolves(self):
        url = reverse('accounts:student_register')
        self.assertEquals(resolve(url).func,student_register)

    def test_student_profile_url_is_resolves(self):
        url = reverse('accounts:student_profile',args= '1')
        self.assertEquals(resolve(url).func,student_profile)

    def test_edit_student_url_is_resolves(self):
        url = reverse('accounts:edit_student')
        self.assertEquals(resolve(url).func,edit_student)

    def test_teacher_register_url_is_resolves(self):
        url = reverse('accounts:teacher_register')
        self.assertEquals(resolve(url).func,teacher_register)

    def test_teacher_profile_url_is_resolves(self):
        url = reverse('accounts:teacher_profile',args = [1])
        self.assertEquals(resolve(url).func,teacher_profile)

    def test_edit_teacher_url_is_resolves(self):
        url = reverse('accounts:edit_teacher')
        self.assertEquals(resolve(url).func,edit_teacher)
