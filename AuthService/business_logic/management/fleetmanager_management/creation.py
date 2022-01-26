from core.management.creation import Creator
from authentication.models import FleetManager

class FleetManagerCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        staff = FleetManager.objects.create(user=user)
        return staff
