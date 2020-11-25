from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my/<str:city>', views.myCity, name ='city'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('student', views.student_list, name='student_list')
]


