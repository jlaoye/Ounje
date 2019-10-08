from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    LOGIN_REDIRECT_URL = 'merchant/home.html'

@login_required(login_url='/merchant_signin')
def merchant_home(request):
    return render(request, 'merchant/home.html')
