from django.shortcuts import render, redirect
from .models import Position, Apply
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser
# Create your views here.


def main_page(request):
    return render(request,"index.html")

def reg_page(request):
    return render(request,"registration.html")

def login_page(request):
    if request.method == 'POST': # VANNAK BELÉPÉSI ADATOK
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pword = form.cleaned_data.get('password')
            user = authenticate(request, username=uname, password=pword)
            if user is not None:
                login(request, user)
                return redirect('jobs')
        return render(request, 'login.html')
    
    else: # ELŐSZÖR JÁR A LOGIN OLDALON
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_page(request):
    logout(request)
    return redirect('index')

#Felvett és a meghirdetett állások
def list_positions(request):
	position_list = Position.objects.all()
    
	applied_jobs = []
	if(not isinstance(request.user, AnonymousUser)):
		applied_jobs = Apply.objects.filter(User_Name=request.user)
	return render(request,"jobs.html",{"position_list": position_list, "applied":applied_jobs})

def applyPosition(request, positionId):
    user = request.user
    position = Position.objects.get(id=positionId)
    apply = Apply(User_Name=user, Pos_Name=position)
    apply.save()
    return redirect('jobs')

def error_page(request):
    return render(request,"404.html")

