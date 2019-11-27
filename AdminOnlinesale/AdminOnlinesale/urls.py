"""AdminOnlinesale URL Configuration

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
from coustemer import urls as cos
from Admin import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',TemplateView.as_view(template_name="login.html"),name='main'),
    path('checkadmin/',views.checkAdmin,name='checkadmin'),
    path('addmerchant/',views.paswordAuto,name='addmerchant'),
    path('savemerchant/',views.savemerchant,name='savemerchant'),
    path('viewmerchant/',views.viewmerchant,name='viewmerchant'),
    path('delte/',views.delte,name='delte'),
    path('checkmerchant/<str:uid>/<str:upass>/',views.CheckPassword.as_view()),
    path('changepsd/<str:emailid>/',views.ChangePsd.as_view()),
    path('Addproduct/',views.Addproduct.as_view()),
    path('sendallproduct/<int:mer_id>/',views.SendProduct.as_view()),
    path('sendproduct/<int:product_id>/',views.SendOneProduct.as_view()),
    path('',include(cos))

]
