from core.management.retrieval import Retriever
from authentication.models import FleetManager


class FleetManagerRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = FleetManager.objects.get(id=instance_id)
        return instance
