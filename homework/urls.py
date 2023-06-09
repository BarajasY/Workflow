from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:homework_id>/", views.detail, name="detail"),
    path("request/", views.homeworkRequest, name="homeworkRequest")
]
