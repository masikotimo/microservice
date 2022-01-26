"""
    Staff Account Managers
"""
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

from business_logic.management.fleetmanager_management import FleetManagerManager
from business_logic.management.user_management import UserManager
from business_logic.utilities.mailing import EmailVerificationLinkSender
from core.utilities.auth import get_authenticated_user

from authentication._serializers import user_serializers

RegisterUserSerializer = user_serializers.RegisterUserSerializer


class AccountCreator():

    def create(self, request):
        """
        A method for registering a carbooking fleetmanager member
        """
        try:
            validated_data = request['validated_data']
            request = request['request']
            email = validated_data.get('email')
            user_cont = UserManager().get_list().filter(email=email).count() or 0
            if user_cont < 1:
                user = RegisterUserSerializer().create(validated_data)
            user = UserManager().get_list().filter(email=email)[0]
            fleetmanager_count = FleetManagerManager().get_list().filter(user=user).count() or 0

            if fleetmanager_count > 0:
                response_data = {
                    'email': [
                        'Staff with this email address (' +
                        email + ') already exists.'
                    ]
                }
                return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.is_fleetmanager = True
                user.save()
                validated_data = {'user': user}
                fleetmanager = FleetManagerManager().create(validated_data)
                authenticated_user = get_authenticated_user(
                    request)  # or AnonymousUser
                if authenticated_user.__str__() == 'AnonymousUser':
                    authenticated_user = user
                print(authenticated_user)
                fleetmanager.registered_by = authenticated_user
                fleetmanager.lastupdated_by = authenticated_user
                fleetmanager.save()
                return EmailVerificationLinkSender(request).send()
        except Exception as exception:
            raise exception
