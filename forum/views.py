from django.shortcuts import render
from django.views.generic import DetailView
from .forms import LoginForm, UserRegistrationForm, DashboardForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Message


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return updateMessage(request)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'forum/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'forum/register.html', {'user_form': user_form})


class MessageDetailView(DetailView):
    model = Message
    template_name = 'dashboard.html'
    qs = Message.objects.all()

    def latest_message(self):
        return Message.objects.last()


def updateMessage(request):
    formbtn = DashboardForm(request.POST)
    message = Message.objects.last()
    if request.method == 'POST' and formbtn.is_valid():
        message.mes = formbtn.cleaned_data['btn']
        if message.mes == "sis":
            message.numberSis += 1
        else:
            message.numberBro += 1
        message.user = request.user.username
        message.save()
        return render(request, 'forum/dashboard.html', {'section': 'dashboard','name': message.user, 'date': message.time, 'mes': message.mes, 'bro': message.numberBro, 'sis': message.numberSis })
    return render(request, 'forum/dashboard.html', {'section': 'dashboard', 'name': message.user, 'date': message.time, 'mes': message.mes, 'bro': message.numberBro, 'sis': message.numberSis } )