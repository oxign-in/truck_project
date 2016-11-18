from rest_framework import serializers
from apps.users.models import User

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    phone = serializers.RegexField("^[789]\d{9}", required=True)

    def validate_username(self, source):
        username = source
        try :
            user = User.objects.get(username=username)
        except:
            return source;
        if user:
            raise serializers.ValidationError("Username already exists. Select another name")
        return source;

    def validate_phone(self, source):
        username = source
        try :
            user = User.objects.get(username=username)
        except:
            return source;
        if user:
            raise serializers.ValidationError("Username already exists. If you have forgot the password, try resetting the password")
        return source;