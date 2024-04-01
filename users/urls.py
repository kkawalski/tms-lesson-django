from django.urls import path

from users.views import (
    MyProfileView,
    LoginView, 
    RegisterView, 
    LogoutView
)


urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("me", MyProfileView.as_view(), name="me"),
]
