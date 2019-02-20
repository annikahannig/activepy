
"""
Active Dispatch
---------------

Implements a dispatch registry.
"""

__handlers = []


def register_handler(handler):
    """Register handler"""
    global __handlers
    __handlers.append(handler)


def make_dispatch(command):
    """Create dispatch function Dispatch to all handlers"""
    # Todo: huh why did I want to keep the command?
    #       Maybe logging?
    def dispatch(action):
        """Dispatch function"""
        for handler in __handlers:
            handler(action)

    return dispatch
