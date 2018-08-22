from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^idealweight/', views.ideal_weight)
]
