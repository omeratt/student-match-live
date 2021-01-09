from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from .. import views

class TestUrls(SimpleTestCase):


    def test_ListPosts_url_is_resolves(self):
        url = reverse('posts:all')
        self.assertEquals(resolve(url).func.view_class,views.PostList)


    def test_CreatePost_url_is_resolves(self):
        url = reverse('posts:create')
        self.assertEquals(resolve(url).func.view_class,views.CreatePost)


    def test_user_post_url_is_resolves(self):
        url = reverse('posts:for_user',args = ['3'])
        self.assertEquals(resolve(url).func.view_class,views.UserPosts)


    def test_delete_url_is_resolves(self):
        url = reverse('posts:delete',args = ['1'])
        self.assertEquals(resolve(url).func.view_class,views.DeletePost)
