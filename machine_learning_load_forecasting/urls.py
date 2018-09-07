from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^excel/', views.list_data),
    url(r'^sklearn/', views.sklearn),
    url(r'^numpy/', views.numpy),
    url(r'^insert_data/', views.insert_data)
]
