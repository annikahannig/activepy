
"""
Test command wrapping
"""

from mock import patch, MagicMock

from active.commands import command


@patch("active.commands.make_dispatch")
def test_command_decorating(make_dispatch):
    """Test decoraing a function"""

    @command
    def cmd(dispatch, request):
        assert isinstance(dispatch, MagicMock)

    # Check that our dispatch is created
    cmd(None)
    assert make_dispatch.called

