
"""
Test action class
"""

from active.actions import Action

def test_action___getattr__():
    """Test getting attributes from action"""
    action = Action(foo=23, bar="fourtytwo")

    assert action.foo == 23
    assert action.bar == "fourtytwo"


def test_action___getitem__():
    """Get item access"""
    action = Action(foo=23, bar="fourtytwo")

    assert action["foo"] == 23
    assert action["bar"] == "fourtytwo"


def test_action___repr__():
    """Test string representation"""
    action = Action(foo=23, bar="fourtytwo")
    assert repr(action)

