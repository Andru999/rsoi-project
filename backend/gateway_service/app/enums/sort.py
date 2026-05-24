from enum import Enum


class SortFlights(Enum):
    IdAsc = "id_asc"
    IdDesc = "id_desc"

    FlightNumberAsc = "flight_number_asc"
    FlightNumberDesc = "flight_number_desc"

    FromAirportmAsc = "from_airport_asc"
    FromAirportDesc = "from_airport_desc"

    ToAirportmAsc = "to_airport_asc"
    ToAirportDesc = "to_airport_desc"

    DateAsc = "date_asc"
    DateDesc = "date_desc"

    PriceAsc = "price_asc"
    PriceDesc = "price_desc"
