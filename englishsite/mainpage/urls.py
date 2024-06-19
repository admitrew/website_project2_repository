from mainpage import views
from django.urls import include, path
from .views import register

urlpatterns = [
    path('', views.mainview, name="main"),
    path('register/', register, name='register'),
]