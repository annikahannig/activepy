
"""
Active Action
-------------

An active action is just a wrapping class
and should encapsulate Requests and Success
or error Actions.
"""

class Action:
    """
    The action base class.
    Encapsulate provided parameters.

    Requests and actions passed to hanlders or commands
    should inherit from Action.

    Exmaple:
        class CreateUserRequest(Action):
            pass
        class CreateUserSuccess(Action):
            pass
        class CreateUserError(Action):
            pass
    """
    def __init__(self, *args, **kwargs):
        """Include kwargs as attributes"""
        self.attributes = kwargs

    def __getattr__(self, key):
        return self.attributes.get(key)

    def __getitem__(self, key):
        return self.attributes.get(key)

    def __repr__(self):
        return f"<Action attributes={str(self.attributes)}>"
