from theorypage import views
from django.urls import include, path

urlpatterns = [
    path('theory-1', views.theory1view, name="theory1"),
]