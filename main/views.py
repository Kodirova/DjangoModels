from django.http import HttpResponse



# Create your views here.
from django.shortcuts import render

from main.models import Student


def index(request):
    return HttpResponse('Hello world')


def myCity(request, city):
    return HttpResponse(f'Your city is {city}')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def student_list(request):
    data = Student.objects.all()
    first_data= Student.objects.first()
    return render(request, 'student.html', {'data': data, 'data2': first_data})









