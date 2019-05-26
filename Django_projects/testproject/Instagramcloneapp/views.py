from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def signup_view(request):
    if request.method == "GET":
        signup_form  = SignUpForm()
    elif request.method == "POST":
        print("Sign up form submitted")
    return render(request, 'index.html',{'signup_form': signup_form})
    