import pytest
from app import App



def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World. Type 'exit' to exit." in out
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Exiting..." in out
