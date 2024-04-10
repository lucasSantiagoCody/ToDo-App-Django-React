from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):

    def create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        self.create_user(
            email=email, 
            username=username,
            password=password,
            **extra_fields
        )