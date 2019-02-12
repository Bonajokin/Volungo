from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse

# Create your views here.
#class SignUpPage(TemplateView):
def get(self, request, **kwargs):
	return render(request, 'index.html', context =None)

def TestingStuff(request):
	return HttpResponse("Testing work")