from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'merchant/home.html')

@login_required(login_url='merchant/sign-in.html')

def merchant_home(request):
    return render(request, 'merchant/home.html')

#def merchant_signin(request):
    #return render(request, '/merchant/sign-in.html')
