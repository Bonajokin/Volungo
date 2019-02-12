from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
	
	# password = forms.CharField(widget=forms.PasswordInput)
	# password2 = forms.CharField(widget=forms.PasswordInput)




	class Meta:
		model = User
		fields = ['username', 'email','first_name', 'password', 'last_name']
		widgets = {
			'username': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder' : 'username'}
			),
			'password': forms.PasswordInput(
				attrs={'class': 'form-control', 'placeholder' : 'password'}
			),
			# 'password2': forms.PasswordInput(
			# 	attrs={'class': 'form-control', 'placeholder': 'confirm password'}
			# ),
			'email' : forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': 'email'}
			),
			'first_name' : forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': 'full name'}
			),
			 'last_name' : forms.HiddenInput(
			 	attrs={}
			 ),



		}
	# #Validate password
	# def clean_password2(self):
	# 	cd = self.cleaned_data
	# 	if cd['password2'] != cd['password']:
	# 		raise ValidationError("Passwords don't match")
    #
	# 	return cd['password2']
		