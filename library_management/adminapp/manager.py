from django.contrib.auth.base_user import BaseUserManager


class AdminManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        admin = self.model(
            email=self.normalize_email(email),
        )
        admin.set_password(password)
        admin.admin = True #Here our entity is also admin
        admin.is_staff = True
        admin.save()
        return admin

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        admin = self.create_user(
            email,
            password=password,
        )
        admin.admin = True
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_active = True
        admin.save()
        return admin
