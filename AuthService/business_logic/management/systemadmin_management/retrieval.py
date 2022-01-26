from core.management.retrieval import Retriever
from authentication.models import SystemAdmin


class SystemAdminRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = SystemAdmin.objects.get(id=instance_id)
        return instance
