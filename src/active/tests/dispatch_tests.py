
"""
Test event dispatching
"""

import mock

from active.dispatch import make_dispatch
from active.handlers import handler
from active.actions import Action


def test_make_dispatch():
    """Test making a dispatch"""
    class FooAction(Action): pass

    handle_foo = mock.MagicMock()
    handler(FooAction)(handle_foo)

    dispatch = make_dispatch(None)
    dispatch(FooAction())

    assert handle_foo.called
