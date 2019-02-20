
"""
Test handler decorator
"""

from mock import patch

from active.actions import Action
from active.handlers import handler


def test_handler_filter():
    """Test handler decoration"""
    class FooAction(Action): pass
    class BarAction(Action): pass

    @handler(FooAction)
    def some_handler(action):
        assert isinstance(action, FooAction)

    handler(FooAction())
    handler(BarAction()) # ignored.


@patch("active.handlers.register_handler")
def test_handler_registration(register_handler):
    """Test handler registration"""
    class FooAction(Action): pass

    @handler(FooAction)
    def some_handler(action):
        pass

    assert register_handler.called
