# yourapp/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PhoneNumberOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check by username or phone number
        try:
            # Try to get user by username first
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                # Try to get user by phone number
                user = UserModel.objects.get(phone_number=username)
            except UserModel.DoesNotExist:
                return None

        # Check if password is correct
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
