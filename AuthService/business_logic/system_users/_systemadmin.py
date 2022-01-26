from . import _user
User = _user.User


class SystemAdmin(User):
    """
    A controller for SystemAdmin as a system user.
    """

    def __init__(self,):
        super()

    # Mutators

    # Accessors

    # Generic User Operations
    def register_systemadmin(self, validated_data):
        return self.get_accounts_controller().register_systemadmin(validated_data)
