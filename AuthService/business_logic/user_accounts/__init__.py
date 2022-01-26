from ._driver_accout import AccountManager as DriverAccountManager
from ._fleetmanager_accout import AccountManager as FleetManagerManager
from ._systemadmin_accout import AccountManager as SystemAdminAccountManager
from ._passenger_accout import AccountManager as PassengerAccountManager


class UserAccountsController():
    _driver_account_manager: None
    _passenger_account_manager: None
    _systemadmin_account_manager: None
    _fleetmanager_account_manager: None

    def set_driver_account_manager(self, driver_account_manager):
        self._driver_account_manager = driver_account_manager

    def get_driver_account_manager(self):
        return self._driver_account_manager

    def set_passenger_account_manager(self, passenger_account_manager):
        self._passenger_account_manager = passenger_account_manager

    def get_passenger_account_manager(self):
        return self._passenger_account_manager

    def set_systemadmin_account_manager(self, systemadmin_account_manager):
        self._systemadmin_account_manager = systemadmin_account_manager

    def get_systemadmin_account_manager(self):
        return self._systemadmin_account_manager

    def set_fleetmanager_account_manager(self, fleetmanager_account_manager):
        self._fleetmanager_account_manager = fleetmanager_account_manager

    def get_fleetmanager_account_manager(self):
        return self._fleetmanager_account_manager

    # Operations
    def register_driver(self, request):
        self.set_driver_account_manager(DriverAccountManager())
        return self._driver_account_manager.register_driver(request)

    def register_fleetmanager(self, request):
        self.set_fleetmanager_account_manager(FleetManagerManager())
        return self._fleetmanager_account_manager.register_fleetmanager(request)

    def register_systemadmin(self, request):
        self.set_systemadmin_account_manager(SystemAdminAccountManager())
        return self._systemadmin_account_manager.register_systemadmin(request)

    def register_passenger(self, request):
        self.set_passenger_account_manager(PassengerAccountManager())
        return self._passenger_account_manager.register_passenger(request)
