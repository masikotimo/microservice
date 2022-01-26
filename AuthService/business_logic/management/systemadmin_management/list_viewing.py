from core.management.list_viewing import ListViewer
from authentication.models import SystemAdmin


class SystemAdminListViewer(ListViewer):

    def get_list(self):
        return SystemAdmin.objects.all()
