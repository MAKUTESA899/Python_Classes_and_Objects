import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercises.exercise2_bank_account import BankAccount

def test_initial_balance():
    account = BankAccount("123456")
    assert account.balance == 0.0

def test_deposit():
    account = BankAccount("123456")
    account.deposit(100.0)
    assert account.balance == 100.0

def test_withdraw():
    account = BankAccount("123456")
    account.deposit(100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0

def test_withdraw_insufficient_funds():
    account = BankAccount("123456")
    with pytest.raises(ValueError, match='Insufficient funds'):
        account.withdraw(50.0)