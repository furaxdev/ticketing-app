
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
from .models import NewUser


def check_user(user):
    return not user.is_authenticated


user_logout_required = user_passes_test(check_user, '/', None)


def auth_user_should_not_access(viewfunc):
    return user_logout_required(viewfunc)


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['user_name'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Username'
        })
        self.fields['user_name'].label = ""
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'First Name'
        })
        self.fields['first_name'].label = ""

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Last Name'
        })
        self.fields['last_name'].label = ""

        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Email'
        })
        self.fields['email'].label = ""

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Password'
        })
        self.fields['password1'].label = ""

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Password Confirmation'
        })
        self.fields['password2'].label = ""

        self.fields['password2'].help_text = ""
        self.fields['password1'].help_text = ""

    class Meta:
        model = NewUser
        fields = ['first_name',
                  'last_name', 'user_name', 'email',  'password1', 'password2']


@auth_user_should_not_access
def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password is incorrect')

    return render(request, 'login.html', {})


def logoutView(request):
    logout(request)
    return redirect('home')


@auth_user_should_not_access
def registerPage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'register.html', context)
