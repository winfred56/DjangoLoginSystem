from django.shortcuts import render,redirect
from .models import UserDetails
from django.contrib.auth.decorators import login_required
from .forms import SignupForms

@login_required
def homeview(request):
    return render(request, 'LoginSystem/home.html')

def signupview(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignupForms()
    return render(request, 'LoginSystem/signup.html', {'form':form})
