from core.management import AbstractManager

from .creation import FleetManagerCreator as Creator
from .list_viewing import FleetManagerListViewer as ListViewer
from .retrieval import FleetManagerRetriever as Retriever
from .updating import FleetManagerUpdater as Updater
from .patching import FleetManagerPatcher as Patcher
from .deletion import FleetManagerDeleter as Deleter


class FleetManagerManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
