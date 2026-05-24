from enum import Enum

from schemas.response import (
    ErrorResponse,
    ForbiddenResponse,
    NotAuthorizedResponse,
    ValidationErrorResponse,
)


class RespFlightEnum(Enum):
    GetAll = {
        "description": "All Flights",
    }
    GetByID = {
        "description": "Flight by ID",
    }
    Created = {
        "description": "Created new Flight",
        "headers": {
            "Location": {
                "description": "Path to new Flight",
                "style": "simple",
                "schema": {
                    "type": "string",
                },
            },
        },
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Delete = {
        "description": "Flight by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Patch = {
        "description": "Flight by ID was updated",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Flight by ID",
    }
    Conflict = {
        "model": ErrorResponse,
        "description": "Conflict",
    }
    NotAuthorized = {
        "model": NotAuthorizedResponse,
        "description": "User is not authorized",
    }
    Forbidden = {
        "model": ForbiddenResponse,
        "description": "Method forbidden to access",
    }


class RespAirportEnum(Enum):
    GetAll = {
        "description": "All Airports",
    }
    GetByID = {
        "description": "Airport by ID",
    }
    Created = {
        "description": "Created new Airport",
        "headers": {
            "Location": {
                "description": "Path to new Airport",
                "style": "simple",
                "schema": {
                    "type": "string",
                },
            },
        },
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Delete = {
        "description": "Airport by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Patch = {
        "description": "Airport by ID was updated",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Airport by ID",
    }
    Conflict = {
        "model": ErrorResponse,
        "description": "Conflict",
    }
    NotAuthorized = {
        "model": NotAuthorizedResponse,
        "description": "User is not authorized",
    }
    Forbidden = {
        "model": ForbiddenResponse,
        "description": "Method forbidden to access",
    }


class RespManageEnum(Enum):
    Health = {
        "description": "Flight server is ready to work",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
