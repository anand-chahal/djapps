from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from auth.views import AuthView


class RegisterView(AuthView):
    def post(self, request):
        if request.method == "POST":
            user_name = request.POST.get("email")
            password = request.POST.get("password")

        # Check if a user with the same username or email already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "User already exists, try logging in.")
            return redirect("register")

        # Create the user and set their password
        created_user = User.objects.create_user(
            username=user_name, email=user_name, password=password
        )
        created_user.set_password(password)
        created_user.save()

        # Add the user to the 'client' group (or any other group you want to use as default for new users)
        user_group, _ = Group.objects.get_or_create(name="client")
        created_user.groups.add(user_group)

        messages.success(
            request,
            f"User with email {user_name} successfully created. Please login now",
        )

        return redirect("register")
