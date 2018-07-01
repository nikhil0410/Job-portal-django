"""coalshastra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from .views import home_page, LoginView, RegisterView
from jobs.views import jobView,post_job,job_view,applied_job,job_application

urlpatterns = [
	url(r'^$', home_page, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^list/$', job_view, name='list'),
    url(r'^postjob/$', post_job, name='postjob'),
    url(r'^applied-job/$', applied_job, name='applied-job'),
    url(r'^job-application/$', job_application, name='job-application'),
]
