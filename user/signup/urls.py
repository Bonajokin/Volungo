from django.conf.urls import url
from user.signup.views import RegisterUser

urlpatterns = [
	#url(r'^$', views.SignUpPage.as_view()),

	url(r'^$', view=RegisterUser.as_view(), name='register'),
]