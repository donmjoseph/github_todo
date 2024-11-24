import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import calculator
import pytest

# Mock input/output for testing
def mock_input_output(inputs):
    def mock_input(prompt):
        return inputs.pop(0)
    return mock_input

def test_addition(monkeypatch, capsys):
    inputs = ["1", "5", "3", "5"]
    monkeypatch.setattr("builtins.input", mock_input_output(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "The result is: 8.0" in captured.out

def test_invalid_option(monkeypatch, capsys):
    inputs = ["10", "5"]
    monkeypatch.setattr("builtins.input", mock_input_output(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
