from django.conf.urls import url
from django.contrib import admin
from MyApp import views

urlpatterns = [
    url(r'^admin-my-app/', admin.site.urls),
    url(r'^ideal-weight/', views.ideal_weight)
]
