from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db import models
import random
from news.models import tip_model



class TestPage(TemplateView):
    template_name = 'test.html'

class ThankPage(TemplateView):
    template_name = 'thanks.html'


def Welcome_view(request):
    items = tip_model.objects.all()

    random_item = random.choice(items)

    context = {
        "popup": random_item.text,
    }
    if request.user.is_authenticated:
        return render(request,'index.html',context)
    else:
        return render(request,'landing_page.html')




# from django.views.generic import TemplateView
# from django.shortcuts import render, redirect
#
# class TestPage(TemplateView):
#     template_name = 'test.html'
#
# class ThankPage(TemplateView):
#     template_name = 'thanks.html'
#
# class HomePage(TemplateView):
#     template_name = 'index.html'
#
# def Welcome_view(request):
#     if request.user.is_authenticated:
#         return render(request,'index.html')
#     else:
#         return render(request,'landing_page.html')
