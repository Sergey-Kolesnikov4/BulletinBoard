from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import random

from .models import OneTimeCode
from .forms import SignupForm, CodeForm, LoginUserForm


def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            one_time_code = OneTimeCode.objects.create(code=random.randint(1000, 9999),user=user)

            mail_subject = 'Подтверждение электронной почты'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'code':one_time_code
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('confirmation_code')
    else:
        form = SignupForm()
    return render(request, 'registration.html', {'form': form})


def confirmation(request):
    if request.method == 'POST':
        form = CodeForm(request)
        code_obj = OneTimeCode.objects.get(user_id__username=request.POST['username'])
        user_code = code_obj.code
        if request.POST['code']==user_code:
            code_obj.user.is_active=True
            code_obj.user.save()
            return redirect('ads_list')
        else:
            return HttpResponse('Код подтверждения неверный')
    else:
        form = CodeForm()
    return render(request, 'confirmation.html', {'form': form})



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

class LogoutUser(LogoutView):
    next_page = '/ads'

def about(request):
    return render(request, 'logout.html', )




