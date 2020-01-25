from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has Been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password'])
                auth.login(request, user)
                return redirect('details') #have to change to details page

        else:
            return render(request, 'signup.html', {'error':'Password doesnt match'})

    else:
        return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['passwordinput'])
        if user is not None:
            auth.login(request, user)
            return redirect('home') #personal Dashboard
        else:
                return render(request, 'login.html', {"error":"Username or Password is invalid"})

    else:
        return render(request, 'login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
