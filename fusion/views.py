from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Home,Services,About,Feedback,Team,Pricing,Testimonial,Features,Featuresimg, Featuresrght,Footer1,Footer,FooterContact,Copyright
from .forms import FeedbackForm,SignUpForm
import json
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User



# Create your views here.
def indexx(request):
     home =Home.objects.all()
     items = Services.objects.all()
     data = About.objects.all()
     dta = Team.objects.all()
     dtaa = Pricing.objects.all()
     dataa = Testimonial.objects.all()
     itemss = Features.objects.all()
     a = Featuresrght.objects.all()
     itmss = Featuresimg.objects.all()
     itms = Footer1.objects.all()
     itm = Footer.objects.all()
     it = FooterContact.objects.all()
     its = Copyright.objects.all()
     context = {
            'home':home,
            'items': items,
            'data': data,
            'dta':dta,
            'dtaa':dtaa,
            'dataa':dataa,
            'itemss': itemss,
            'itmss': itmss,
            'a': a,
            'itms': itms,
            'itm': itm,
            'it': it,
            'its': its,
        }

     return render(request, 'indexx.html', context=context)     




def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Feedback.objects.create(name=name,message=message,email=email)
    return render(request, "success.html", {'form': form})


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            user= form.save(commit=False)
            # user.refresh_from_db()  # load the profile instance created by the signal
            user.birth_date = form.cleaned_data.get('birth_date')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)) ,
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
          
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.birth_date = form.cleaned_data.get('birth_date')
            # user.save()
            # username = form.cleaned_data.get('username')
            # raw_password  = form.cleaned_data.get('password1')
            # email = form.cleaned_data.get('email')
            # user = authenticate(username=username,  password=raw_password,email=email)
            # login(request, user)
            # return redirect('login')
    else:
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')