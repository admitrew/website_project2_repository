from lessonpage import views
from django.urls import include, path

urlpatterns = [
    path('lesson-2', views.lesson2view, name="lesson2"),
]