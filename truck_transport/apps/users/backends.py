from django.conf import settings
from .models import User

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username__iexact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(email__iexact=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
