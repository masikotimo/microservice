from core.management.list_viewing import ListViewer
from authentication.models import FleetManager


class FleetManagerListViewer(ListViewer):

    def get_list(self):
        return FleetManager.objects.all()
