from theorypage import views
from django.urls import include, path

urlpatterns = [
    path('', views.theoryview, name="theory"),
]