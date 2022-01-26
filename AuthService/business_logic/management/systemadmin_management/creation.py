from core.management.creation import Creator
from authentication.models import SystemAdmin


class SystemAdminCreator(Creator):

    def create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        courier = SystemAdmin.objects.create(user=user)
        return courier
