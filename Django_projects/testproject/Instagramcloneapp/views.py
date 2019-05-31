from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def signup_view(request):
    signup_form = ''
    if request.method == "GET":
        signup_form  = SignUpForm()
    elif request.method == "POST":
        print("form submitted")
            
    return render(request, 'index.html',{'signup_form': signup_form})
    