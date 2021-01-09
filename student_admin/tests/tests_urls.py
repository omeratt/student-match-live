from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from ..views import Welcome_view,ThankPage,TestPage

class TestUrls(SimpleTestCase):

    def test_welcome_url_is_resolves(self):
        url = reverse('Welcome_View')
        self.assertEquals(resolve(url).func,Welcome_view)

    def test_test_direct_url_is_resolves(self):
        url = reverse('test')
        self.assertEquals(resolve(url).func.view_class,TestPage)

    def test_thanks_direct_url_is_resolves(self):
        url = reverse('thanks')
        self.assertEquals(resolve(url).func.view_class,ThankPage)
