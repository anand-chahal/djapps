from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from auth.views import AuthView


class LoginView(AuthView):
    def post(self, request):
        if request.method == "POST":
            user_name = request.POST.get("email")
            password = request.POST.get("password")

            user = User.objects.filter(username=user_name).first()
            if user is None:
                messages.error(request, "Invalid email! Please enter a valid email")
                return redirect("login")

            authenticated_user = authenticate(
                request, username=user_name, password=password
            )
            if authenticated_user is not None:
                # Login the user if authentication is successful
                login(request, authenticated_user)

                # Redirect to the page the user was trying to access before logging in
                if "next" in request.POST:
                    return redirect(request.POST["next"])
                else:  # Redirect to the home page or another appropriate page
                    return redirect("index")
            else:
                messages.error(request, "Invalid password!")
                return redirect("login")
