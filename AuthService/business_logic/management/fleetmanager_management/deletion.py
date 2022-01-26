from core.management.deletion import Deleter
from authentication.models import FleetManager


class FleetManagerDeleter(Deleter):

    def delete(self, instance_id):
        return FleetManager.objects.delete(id=instance_id)
