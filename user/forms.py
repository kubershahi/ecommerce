from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from user.models import User


class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(label = 'First name', widget= forms.TextInput(attrs={'placeholder':'First name'}))
	last_name = forms.CharField(label = 'Last name', widget= forms.TextInput(attrs={'placeholder':'Last name'}))
	username = forms.CharField(label = 'Username', widget= forms.TextInput(attrs={'placeholder':'Username'}))
	email = forms.EmailField(max_length=60, label = 'Email address', help_text='Required. Add a valid email address.',widget= forms.EmailInput(attrs={'placeholder':'Email address'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2', )

class LoginForm(forms.ModelForm):
	email = forms.EmailField(max_length=60, label = 'Email address', help_text='Required. Add a valid email address.',widget= forms.EmailInput(attrs={'placeholder':'Email address'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	class Meta:
		model = User
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email',)

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = User.objects.exclude(pk=self.instance.pk).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = User.objects.exclude(pk=self.instance.pk).get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)



