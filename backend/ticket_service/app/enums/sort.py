from enum import Enum


class SortTicket(Enum):
    UsernameAsc = "username_asc"
    UsernameDesc = "username_desc"

    FlightNumberAsc = "flight_number_asc"
    FlightNumberDesc = "flight_number_desc"

    PriceAsc = "price_asc"
    PriceDesc = "price_desc"

    StatusAsc = "status_asc"
    StatusDesc = "status_desc"

    IdAsc = "id_asc"
    IdDesc = "id_desc"
