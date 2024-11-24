from calculator import calculator
import pytest

# Mock input and output for testing
def mock_input_output(inputs):
    def mock_input(prompt):
        return inputs.pop(0)
    return mock_input

def test_addition(monkeypatch, capsys):
    # Simulate user inputs: Option 1, numbers 5 and 3, and exit
    inputs = ["1", "5", "3", "5"]
    monkeypatch.setattr("builtins.input", mock_input_output(inputs))
    
    calculator()
    
    # Capture the output
    captured = capsys.readouterr()
    assert "The result is: 8.0" in captured.out

def test_invalid_option(monkeypatch, capsys):
    inputs = ["10", "5"]
    monkeypatch.setattr("builtins.input", mock_input_output(inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
