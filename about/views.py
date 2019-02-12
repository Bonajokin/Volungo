from django.shortcuts import HttpResponse, render
from user.signup.forms import RegisterUserForm

# Create your views here.

def index(request):
	myform = RegisterUserForm()
	return render(request, 'index.html', {'form': myform})