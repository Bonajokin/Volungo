#import simplejson as simplejson
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseForbidden
from pip._vendor.requests.packages.urllib3 import request
from user.signup.forms import RegisterUserForm
from user.models import User
# Create your views here.
#class SignUpPage(TemplateView):
	#def get(self, request, **kwargs):
	#	return render(request, 'sign-up-page.html', context =None)


class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = "sign-up-page.html"

	'''
	JSONdata = request.POST['data']
	dict = simplejson.JSONDecoder().decode(JSONdata)

	username = dict['id_username']

	def response(self):
		return HttpResponse(username)
		
		'''
	def dispatch(self, request, *args, **kwargs):
		#if request.user.is_authenticated():
		#	return HttpResponseForbidden()

		return super(RegisterUser, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])

		ourUser = User(name=form.cleaned_data['username'], email=form.cleaned_data['email'], gender=form.cleaned_data['last_name'])
		ourUser.save()
		user.save()
		return HttpResponse('User register')



