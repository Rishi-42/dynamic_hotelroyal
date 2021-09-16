from django.shortcuts import render
from .models import Speciality, Meal, Gallery, Feedback


def index(request):
    specialitys = Speciality.objects.all()
    meals = Meal.objects.all()
    gallerys = Gallery.objects.all()
    feedbacks = Feedback.objects.all()
    context = {
        'specialitys' : specialitys,
        'meals' : meals,
        'gallerys' : gallerys,
        'feedbacks' : feedbacks,
    }
    return render(request, 'royal_hotel/index.html', context)

