from core.management.deletion import Deleter
from authentication.models import SystemAdmin


class SystemAdminDeleter(Deleter):

    def delete(self, instance_id):
        return SystemAdmin.objects.delete(id=instance_id)
