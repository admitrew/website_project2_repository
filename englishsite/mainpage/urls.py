from mainpage import views
from django.urls import include, path

urlpatterns = [
    path('', views.mainview, name="main"),
]