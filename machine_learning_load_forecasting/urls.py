from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sl/', views.statistical_learning),
    url(r'^excel/', views.list_data),
    url(r'^read_excel/', views.pandas_read_excel),
    url(r'^knn/', views.knn),
    url(r'^knntt/', views.knn_train_test),
    url(r'^lr/', views.logistic_regression),
    url(r'^lrtt/', views.logistic_regression_train_test),
    url(r'^iris_data/', views.iris_data),
    url(r'^insert_data/', views.insert_data)
]
