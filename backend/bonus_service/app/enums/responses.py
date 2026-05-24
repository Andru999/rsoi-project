from enum import Enum

from schemas.response import (
    ErrorResponse,
    ForbiddenResponse,
    NotAuthorizedResponse,
    ValidationErrorResponse,
)


class RespPrivilegeEnum(Enum):
    GetAll = {
        "description": "All Privileges",
    }
    GetByID = {
        "description": "Privilege by ID",
    }
    Created = {
        "description": "Created new Privilege",
        "headers": {
            "Location": {
                "description": "Path to new Privilege",
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
        "description": "Privilege by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Patch = {
        "description": "Privilege by ID was updated",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Privilege by ID",
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


class RespPrivilegeHistoryEnum(Enum):
    GetAll = {
        "description": "All Privilege Histories",
    }
    GetByID = {
        "description": "Privilege History by ID",
    }
    Created = {
        "description": "Created new Privilege History",
        "headers": {
            "Location": {
                "description": "Path to new Privilege History",
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
        "description": "Privilege History by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
    Patch = {
        "description": "Privilege History by ID was updated",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Privilege History by ID",
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
        "description": "Bonus server is ready to work",
        "content": {
            "application/octet-stream": {
                "example": "",
            },
        },
    }
