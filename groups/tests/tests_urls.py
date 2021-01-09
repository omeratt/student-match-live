from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from groups.views import ListGroups,CreateGroup,SingleGroup,JoinGroup,LeaveGroup
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic

class TestUrls(SimpleTestCase):


    def test_ListGroups_url_is_resolves(self):
        url = reverse('groups:all')
        self.assertEquals(resolve(url).func.view_class,ListGroups)


    def test_CreateGroup_url_is_resolves(self):
        url = reverse('groups:create')
        self.assertEquals(resolve(url).func.view_class,CreateGroup)


    def test_single_url_is_resolves(self):
        url = reverse('groups:single',args = ['f'])
        self.assertEquals(resolve(url).func.view_class,SingleGroup)


    def test_join_url_is_resolves(self):
        url = reverse('groups:join',args = ['f'])
        self.assertEquals(resolve(url).func.view_class,JoinGroup)


    def test_leave_url_is_resolves(self):
        url = reverse('groups:leave',args = ['f'])
        self.assertEquals(resolve(url).func.view_class,LeaveGroup)
