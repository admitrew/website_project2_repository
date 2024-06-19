from lessonpage import views
from django.urls import include, path

urlpatterns = [
    path('lesson-1', views.lesson1view, name="lesson1"),
    path('lesson-2', views.lesson2view, name="lesson2"),
#    path('lesson-3', views.lesson2view, name="lesson3"),
    path('lesson-4', views.lesson4view, name="lesson4"), # NOT WORKING PAGE
    path('lesson-4', views.lesson4view, name='handle_button'), 
#    path('lesson-5', views.lesson2view, name="lesson5"),
]