"""E_Helth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

from helth_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name="main"),
    path('index/',views.home),
    path('adduser/',views.addUser,name='adduser'),
    path('savedata/',views.savedata,name='savedata'),
    path('updateuser/',views.updateuser,name='updateuser'),
    path('updatuno/',views.updatuno,name='updatuno'),
    path('saveupdate/',views.saveupdate,name='saveupdate'),
    path('deleteuno/',views.deleteuno,name='deleteuno'),
    path('addmd/',views.addmd,name='addmd'),
    path('savedatamd/',views.savedatamd,name='savedatamd'),
    path('viewmd/',views.viewmd,name='viewmd'),
    path('updatmd/',views.updatmd,name='updatmd'),
    path('saveupdateMD/',views.saveupdateMD,name='saveupdateMD'),
    path('deletmd/',views.deletmd,name='deletmd')
]
