from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from userpanel.models import User
from .forms import LoginForm, RegistrationForm

# from .forms import ContactForm


def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"Hello World!",
        "content":" Welcome to the homepage.",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHH"
    return render(request, "home_page.html", context)

class LoginView(FormView):
	form_class = LoginForm
	success_url = '/'
	template_name = 'login.html'

	def form_valid(self,form):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user_details = User.objects.filter(email=username)
		print(user_details)
		request = self.request
		user = authenticate(request,username=username, password=password)
		login(request,user)
		return redirect('/')

class RegisterView(FormView):
	form_class = RegistrationForm
	template_name = 'register.html'
	success_url='/login'

	def form_valid(self,form):
		request = self.request
		# f = JobForm(request.POST)
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				print(form)
				instance = form.save(commit=True)
		return redirect('/')
