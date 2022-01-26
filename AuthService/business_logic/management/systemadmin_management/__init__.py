from core.management import AbstractManager

from .creation import SystemAdminCreator as Creator
from .list_viewing import SystemAdminListViewer as ListViewer
from .retrieval import SystemAdminRetriever as Retriever
from .updating import SystemAdminUpdater as Updater
from .patching import SystemAdminPatcher as Patcher
from .deletion import SystemAdminDeleter as Deleter


class SystemAdminManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
