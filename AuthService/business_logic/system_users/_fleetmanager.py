from . import _user
User = _user.User

class FleetManager(User):
    """
    A controller for FleetManager as a system user.
    """
    def __init__(self,):
        super()

    # Mutators

    # Accessors 

    # Generic User Operations
    def register_fleetmanager(self, validated_data):
        return self.get_accounts_controller().register_fleetmanager(validated_data)
