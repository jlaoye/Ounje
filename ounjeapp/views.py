from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from ounjeapp.forms import UserForm, MerchantForm

# Create your views here.
def home(request):
    return redirect(merchant_home)

#@login_required -- no need as we are already asking for login in home.html
def merchant_home(request):
        return render(request, 'merchant/home.html')

# update alternate flow at later time to show exceptions
    #else:
    #    return HttpResponse('Invalid log in!')

def merchant_logout(request):
  return logout(request)

# --def register(request):
#    if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            username = form.cleaned_data.get('username')
#            login(request, user)
#            return redirect(merchant_home)
#        else:
#            for msg in form.error_messages:
#                print(form.error_messages[msg])
#            return render(request = request,
#                  template_name = "registration/register.html",
#                  context={"form": form})

#    form = UserCreationForm
#    return render(request = request,
#          template_name = "registration/register.html",
#          context={"form": form})

def restaurant_signUp(request):
    user_form = UserForm()
    restaurant_form = MerchantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = MerchantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = merchant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()


            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(merchant_home)

    return render(request, 'registration/signup.html', {
            "user_form": user_form,
            "restaurant_form": restaurant_form
    })
#def merchant_signin(request):
    #    username = request.POST.get('username')
    ##    user = authenticate (username=username, password=password)
    #    if user is not None:
    #        login(user)
    #    else:
    #        HttpResponse("Error")
