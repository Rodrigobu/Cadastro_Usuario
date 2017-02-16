from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse

from myuser.forms import UserCreationForm


def home(request):
    return render(request, 'myuser/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('myuser:home'))

    kwargs['extra_context'] = {'next': reverse('myuser:home')}
    kwargs['template_name'] = 'myuser/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('myuser:home')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('myuser:login')
    template_name = "myuser/register.html"
