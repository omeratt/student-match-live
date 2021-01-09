from django.shortcuts import render
from .models import tip_model
import random

def index(request):

    items = tip_model.objects.all()

    random_item = random.choice(items)

    context = {
        "popup": random_item.text,
    }

    return render(request, 'index.html', context)
