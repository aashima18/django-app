from django import forms
from .models import Feedback
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=254)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This email address is already registered.')
        return email




class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'