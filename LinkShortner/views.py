from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request = request, user = form.get_user())
    elif request.method == 'GET':
        form = AuthenticationForm()

    return render(request, template_name = 'linkshortner/login_page.html', context = {
        'form' : form,
        'current_user' : request.user
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('link_shortner:login_view')


def create_short_link(request):
    return render(request, 'linkshortner/create_shortlink.html', context={
        'current_user' : request.user
    })
