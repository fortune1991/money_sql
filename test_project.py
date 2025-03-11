import pytest
import datetime
from project import create_pot, create_vault, create_user
from project_classes import User, Vault, Pot

def test_create_user(monkeypatch):
    # Simulate user input responses
    mock_inputs = iter(["Mike"])

    # return the next input in sequence
    def mock_input(_=None):
        return next(mock_inputs, "DEFAULT")  # Prevent StopIteration errors
    
    # Apply monkeypatch to replace the print_slow function to speed up the test
   
    monkeypatch.setattr("project_functions.print_slow", print)  # Replace with regular print
    monkeypatch.setattr("project.print_slow", print)  # Replace with regular print
    
    # Apply monkeypatch to replace input() calls for create_user function
    monkeypatch.setattr("builtins.input", mock_input)

    # Create mock user

    user = create_user()

    # create_user Assertions 
    assert isinstance(user, User) # create_user should return an instance of User
    assert user.username == "Mike" # user.username should be Mike  

def test_create_vault(monkeypatch):
    # Simulate user input responses
    mock_inputs = iter(["Mike", "Holiday", "25/02/25", "25/03/25", "Holiday", "25/02/25", "25/03/25", "Holiday", "25/02/25", "25/03/25"])

    # return the next input in sequence
    def mock_input(_=None):
        return next(mock_inputs, "DEFAULT")  # Prevent StopIteration errors
    
    # Apply monkeypatch to replace the print_slow function to speed up the test
   
    monkeypatch.setattr("project_functions.print_slow", print)  # Replace with regular print
    monkeypatch.setattr("project.print_slow", print)  # Replace with regular print
    
    # Apply monkeypatch to replace input() calls for create_user function
    monkeypatch.setattr("builtins.input", mock_input)

    # Create mock user

    user = create_user()
 
    # Create mock vault

    vault = create_vault(1, user)  

    # create mock start date

    mock_startdate = datetime.datetime.strptime("25/02/25","%d/%m/%y")

    # create_vault Assertions
    assert isinstance(vault, Vault) # create_vault should return an instance of Vault
    assert vault.vault_name == "Holiday" # vault name should be Holiday
    assert vault.start == mock_startdate
    with pytest.raises(ValueError):
        create_vault(1, "string")
    with pytest.raises(ValueError):
        create_vault("string", user)


def test_create_pot(monkeypatch):
    # Simulate user input responses
    mock_inputs = iter(["Mike", "Holiday", "25/02/25", "25/03/25", "Italy", "25/02/25", "25/03/25", 100.00, 
                        "Italy", "25/02/25", "25/03/25", 100.00, "Italy", "25/02/25", "25/03/25", 100.00])

    # return the next input in sequence
    def mock_input(_=None):
        return next(mock_inputs, "DEFAULT")  # Prevent StopIteration errors
    
    # Apply monkeypatch to replace the print_slow function to speed up the test
   
    monkeypatch.setattr("project_functions.print_slow", print)  # Replace with regular print
    monkeypatch.setattr("project.print_slow", print)  # Replace with regular print
    
    # Apply monkeypatch to replace input() calls for create_user function
    monkeypatch.setattr("builtins.input", mock_input)

    # Create mock user

    user = create_user()
 
    # Create mock vault

    vault = create_vault(1, user)  

    # Create mock pot 
    
    pot = create_pot(1, vault)

    # create mock start date

    mock_startdate = datetime.datetime.strptime("25/02/25","%d/%m/%y")

    # create_vault Assertions
    assert isinstance(pot, Pot) # create_pot should return an instance of Pot
    assert pot.pot_name == "Italy" # vault name should be Holiday
    assert pot.start == mock_startdate
    assert pot.amount == 100.00
    with pytest.raises(ValueError):
        create_pot(1, "string")
    with pytest.raises(ValueError):
        create_pot("string", vault)