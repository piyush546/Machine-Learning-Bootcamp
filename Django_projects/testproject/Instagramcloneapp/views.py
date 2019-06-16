from django.shortcuts import render
from .forms import SignUpForm
from .models import UserModel
#from django.contrib.auth.hashers import make_password
# Create your views here.
def signup_view(request):
    signup_form = ''
    if request.method == "GET":
        signup_form  = SignUpForm()
    elif request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data["username"]
            name = signup_form.cleaned_data["name"]
            email = signup_form.cleaned_data["email"]
            password = signup_form.cleaned_data["password"]
            user = UserModel(name=name, password=password, email = email, username= username)
            user.save()
            return render(request, "success.html")
    return render(request, 'index.html',{'signup_form': signup_form})
    
