from django.shortcuts import render
  
# create a function
def homeView(request):

    return render(request, "index.html")

def loginSignUp(request):

    return render(request, "signin.html")