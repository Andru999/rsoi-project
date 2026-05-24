from enum import Enum


class TicketStatus(str, Enum):
    Paid = "PAID"
    Canceled = "CANCELED"


class PrivilegeStatus(str, Enum):
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"


class PrivilegeHistoryStatus(str, Enum):
    FILL_IN_BALANCE = "FILL_IN_BALANCE"
    DEBIT_THE_ACCOUNT = "DEBIT_THE_ACCOUNT"
