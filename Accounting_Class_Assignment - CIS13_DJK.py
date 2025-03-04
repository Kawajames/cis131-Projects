# File Name: Accounting Class Assignment - CIS131
# Description: This script defines the Account class with read-only properties for name and balance using single leading underscores for attributes.
# Author: Dakota Kartchner 
# Date Created: 2/28/2025

from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')
        
        self._name = name  # Single leading underscore for internal use
        self._balance = balance  # Single leading underscore for internal use

    @property
    def name(self):
        """Return the account holder's name (read-only)."""
        return self._name

    @property
    def balance(self):
        """Return the account balance (read-only)."""
        return self._balance

    def deposit(self, amount):
        """Deposit money to the account."""
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self._balance += amount