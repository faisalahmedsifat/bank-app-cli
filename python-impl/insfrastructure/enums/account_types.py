from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CURRENT = 2
    SALARY = 3
    FIXED = 4
    STUDENT = 5
    OTHERS = 6