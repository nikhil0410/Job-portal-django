from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()

class LoginForm(forms.Form):
	username    = forms.CharField(label='username')
	password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
	password1 = forms.CharField(label='password')
	password2 = forms.CharField(label='Confirm Password')
	user_email = forms.CharField(label='Email')


	class Meta:
		model = User 
		fields = ('full_name', 'email','user_type')


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('password does not match')
		return password2

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user_mail = self.cleaned_data.get('user_email')
		print(user_mail)
		user.set_password(self.cleaned_data['password1'])
		if(commit):
			user.save()

		return user 
