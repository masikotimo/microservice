"""
    Vendor Account Managers
"""
from rest_framework.response import Response
from rest_framework import status

from business_logic.management.systemadmin_management import SystemAdminManager
from business_logic.management.user_management import UserManager
from authentication._serializers import user_serializers
from business_logic.utilities.mailing import EmailVerificationLinkSender
from core.utilities.auth import get_authenticated_user

RegisterUserSerializer = user_serializers.RegisterUserSerializer


class AccountCreator():

    def create(self, request):
        """
        A method for registering a system admin member
        """
        try:
            validated_data = request['validated_data']
            request = request['request']
            email = validated_data.get('email')
            user_cont = UserManager().get_list().filter(email=email).count() or 0
            if user_cont < 1:
                user = RegisterUserSerializer().create(validated_data)
            user = UserManager().get_list().filter(email=email)[0]
            systemadmin_count = SystemAdminManager().get_list().filter(user=user).count() or 0

            if systemadmin_count > 0:
                response_data = {
                    'email': [
                        'Vendor with this email address (' +
                        email + ') already exists.'
                    ]
                }
                return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.is_systemadmin = True
                user.save()
                validated_data = {'user': user}
                systemadmin = SystemAdminManager().create(validated_data)
                authenticated_user = get_authenticated_user(
                    request)  # or AnonymousUser
                if authenticated_user.__str__() == 'AnonymousUser':
                    authenticated_user = user
                print(authenticated_user)
                systemadmin.registered_by = authenticated_user
                systemadmin.lastupdated_by = authenticated_user
                systemadmin.save()
                return EmailVerificationLinkSender(request).send()
        except Exception as exception:
            raise exception
