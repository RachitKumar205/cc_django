from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from django.shortcuts import render

# Create your views here.

@login_required
def index(request):
    return render(request, 'home/index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home/index.html')
    context['form'] = form
    return render(request, 'registration/register.html', context)

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
