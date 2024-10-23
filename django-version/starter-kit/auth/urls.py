from django.urls import path
from django.contrib.auth.views import LogoutView
from .register.views import RegisterView
from .login.views import LoginView
from .forgot_password.views import ForgetPasswordView
from .reset_password.views import ResetPasswordView


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        RegisterView.as_view(template_name="register.html"),
        name="register",
    ),
    path(
        "forgot-password/",
        ForgetPasswordView.as_view(template_name="auth_forgot_password_basic.html"),
        name="forgot-password",
    ),
    path(
        "reset-password/<str:token>/",
        ResetPasswordView.as_view(template_name="reset-password.html"),
        name="reset-password",
    ),
]
