from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^excel/', views.list_data),
    url(r'^insert_data/', views.insert_data)
]
