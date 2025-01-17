from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from user.forms import RegistrationForm, LoginForm, AccountUpdateForm


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('productscreen')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'user/registration.html', context)


def logout_view(request):
	logout(request)
	return redirect('productscreen')


def login_view(request):

	context ={}

	user = request.user
	if user.is_authenticated:
		redirect('productscreen')

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect('productscreen')

	else:
		form = LoginForm()
	
	context['login_form'] = form
	return render(request, 'user/loginpage.html', context)


def account_view(request):

	if not request.user.is_authenticated:
		return redirect('login')
	
	context = {}

	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			context['success_message'] = "Changes updated!"
	else: 
		form = AccountUpdateForm(

			initial={
					"first_name": request.user.first_name,
					"last_name": request.user.last_name,
					"email": request.user.email, 
					"username": request.user.username,
					
				}
			)
	context['account_form'] = form
	return render(request, 'user/myaccount.html', context)


