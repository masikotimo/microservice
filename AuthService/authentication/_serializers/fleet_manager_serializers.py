from rest_framework import serializers

from authentication.models import User, FleetManager
from business_logic.system_users._user import User as UserFacade
from core.mixins.serializer_mixins import ModelSerializer
from business_logic.utilities.mailing import EmailVerificationLinkSender
from .user_serializers import UserProfileSerializer, UserSerializer
from business_logic.auth.authentication import FleetManagerEmailAndPasswordAuthentication


class CreateFleetManagerSerializer(ModelSerializer):
    email = serializers.EmailField(
        max_length=254,
        min_length=5,
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        required=True,
        write_only=True,
        help_text='Required',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    data = serializers.DictField(
        required=False,
        read_only=True,
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'data']

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        return UserFacade().register_fleetmanager(request)


class FleetManagerSerializer(ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = FleetManager
        fields = ['id', 'user', ]
        depth = 2

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class FleetManagerLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        login_data = attrs
        return FleetManagerEmailAndPasswordAuthentication().login(login_data)
