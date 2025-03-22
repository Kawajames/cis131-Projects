# File Name: employee.py - CIS131
# Description: This file defines the abstract base class Employee using Python’s abc module.
# Author: Dakota Kartchner
# Date Created: 3/17/2025

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first, last, ssn):
        self._first = first
        self._last = last
        self._ssn = ssn

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def ssn(self):
        return self._ssn

    @abstractmethod
    def earnings(self):
        # this is a placeholder method
        raise NotImplementedError("earnings method must be defined in subclass")

    def __repr__(self):
        return f"{self.first} {self.last}, SSN: {self.ssn}"