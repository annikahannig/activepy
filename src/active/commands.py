
"""
Active Command
--------------

Decorate a function to act as a command.
This function will receive a dispatch function
to emit events.
"""

from functools import wraps

from active.dispatch import make_dispatch

def command(cmd):
    """
    Decorate a command function and provide a dispatch.
    Make sure the function is unary and only
    accepts a Action.
    """
    # Prepare dispatch function
    dispatch = make_dispatch(cmd)

    @wraps(cmd)
    def _command_wrapper(request):
        """Accept the request and call wrapped function"""
        # Dispatch request
        dispatch(request)

        # Handle request
        return cmd(dispatch, request)

    return _command_wrapper


