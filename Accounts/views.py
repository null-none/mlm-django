from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Personalization.models import UserProfile

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
        except:
            return HttpResponseRedirect("login.html")
        if user is not None and user.is_active:
            return HttpResponseRedirect("/news/")
        else:
            return HttpResponseRedirect("login.html")
    else:
        form = UserCreationForm()
        return render_to_response("login.html",{'form' : form})

def register(request):
    auth.logout(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        data = request.POST.copy()
        new_user = form.save(data)
        profile = UserProfile.objects.create(user = new_user)
        profile.save()
        auth.logout(request)
        return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
        return render_to_response("register.html", {'form' : form})
