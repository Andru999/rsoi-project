from enum import Enum


class TicketStatus(str, Enum):
    Paid = ("PAID",)
    Canceled = "CANCELED"
