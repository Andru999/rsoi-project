from enum import Enum

from schemas.response import (
    ErrorResponse,
    ForbiddenResponse,
    NotAuthorizedResponse,
    ValidationErrorResponse,
)
from schemas.statistics import (
    StatisticsPaginationResponse,
    StatisticsResponse,
)


class ResponseClass(Enum):
    GetAll = {
        "model": StatisticsPaginationResponse,
        "description": "All Statistics",
    }
    GetByID = {
        "model": StatisticsResponse,
        "description": "Statistics by ID",
    }
    Add = {
        "description": "Add new Statistics",
        "headers": {
            "Location": {
                "description": "Path to new Statistics",
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
        "description": "Statistics by ID was deleted",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Statistics by ID",
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
        "description": "Statistics server is ready to work",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
