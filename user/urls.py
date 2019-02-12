from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^register/', include('user.signup.urls')),
	url(r'^register/$', views.TestingStuff, name= 'register')
]