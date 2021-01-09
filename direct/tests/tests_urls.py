from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from direct.views import Inbox,UserSearch,Directs,NewConversation,SendDirect,checkDirects

class TestUrls(SimpleTestCase):


    def test_inbox_url_is_resolves(self):
        url = reverse('inbox')
        self.assertEquals(resolve(url).func,Inbox)

    def test_usersearch_url_is_resolves(self):
        url = reverse('usersearch')
        self.assertEquals(resolve(url).func,UserSearch)

    def test_send_direct_url_is_resolves(self):
        url = reverse('send_direct')
        self.assertEquals(resolve(url).func,SendDirect)

       
