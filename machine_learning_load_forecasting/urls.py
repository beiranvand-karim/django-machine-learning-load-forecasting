from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^excel/', views.list_data),
    url(r'^knn/', views.knn),
    url(r'^logistic_regression/', views.logistic_regression),
    url(r'^iris_data/', views.iris_data),
    url(r'^insert_data/', views.insert_data)
]
