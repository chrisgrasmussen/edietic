"""
URL configuration for eidetic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from start import views
from complete import views as complete_views
from rest_framework.urlpatterns import format_suffix_patterns
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', views.start_list),
    path('start/<int:pk>', views.start_detail),
    path('complete/', complete_views.complete_list),
    path('complete/<int:pk>', complete_views.complete_detail),
    
    # re_path('login', users_views.login), 
    # re_path('signup', users_views.signup),
    # re_path('test_token', users_views.test_token),
    
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("callback/", views.callback, name="callback"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
