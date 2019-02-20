
"""
Active Handler
--------------

Decorate a function to recieve emitted actions.
"""

from functools import wraps

from active.dispatch import register_handler

class handler:
    """
    Handler decorator: Registers the handler in the
    dispatch table and installs a filter for action types.

    Non active.Actions don't pass.
    """
    def __init__(self, *args, **kwargs):
        """Setup handler decorator with action filter"""
        self.action_classes = args

    def __call__(self, handler):
        """Decorate handler function and register handler"""
        # Decorate with filter
        @wraps(handler)
        def _handler_wrapper(action):
            """Filter incoming actions"""
            action_cls = type(action)
            if self.action_classes and not action_cls in self.action_classes:
                return # Nothing to do for us here

            return handler(action)

        # Register handler
        register_handler(_handler_wrapper)

        return _handler_wrapper
