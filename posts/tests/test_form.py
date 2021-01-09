from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from django.contrib.auth.forms import UserCreationForm
from .. import forms
from groups.models import Group
class TestForms(SimpleTestCase,UserCreationForm):

    def test_Post_form_valid(self):
        '''
        cant post on uncreated groups
        '''
        form = forms.PostForm(data={
            'message': 'ss',
            'group': 'ss',
            })
        self.assertFalse(form.is_valid())
