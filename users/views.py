from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    FormView,
)
from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView as DjangoLoginView, 
    LogoutView as DjangoLogoutView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User
from users.forms import (
    LoginForm, 
    RegisterForm, 
    UpdateMyProfileForm
)


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy("home")

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        res = super().form_valid(form)
        login(self.request, form.instance)
        return res


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "login.html"


class LogoutView(DjangoLogoutView):
    pass


class MyProfileView(LoginRequiredMixin, FormView):
    form_class = UpdateMyProfileForm
    template_name = "my_profile.html"
    model = User
    success_url = reverse_lazy("me")

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        return kwargs
    """
    UpdateMyProfileForm(**data, instance=self.request.user)
    """

    def form_valid(self, form: UpdateMyProfileForm) -> HttpResponse:
        form.save(commit=True)
        return super().form_valid(form)
