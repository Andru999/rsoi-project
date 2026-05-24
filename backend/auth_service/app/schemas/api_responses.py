from pydantic import BaseModel, ConfigDict
from utils.enums import DomainEnum


class ApiResponses:
    @staticmethod
    def get_all(domain_name: DomainEnum) -> dict:
        return {
            "description": f"All {domain_name}",
        }

    @staticmethod
    def get_by_uuid(domain_name: DomainEnum) -> dict:
        return {
            "description": f"{domain_name} by uuid",
        }

    @staticmethod
    def create(domain_name: DomainEnum) -> dict:
        return {
            "description": f"Created new {domain_name}",
            "headers": {
                "Location": {
                    "description": f"Path to new {domain_name}",
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

    @staticmethod
    def patch(domain_name: DomainEnum) -> dict:
        return {
            "description": f"{domain_name} by uuid was updated",
        }

    @staticmethod
    def delete(domain_name: DomainEnum) -> dict:
        return {
            "description": f"{domain_name} by uuid was removed",
            "content": {
                "application/octet-stream": {
                    "example": "",
                },
            },
        }

    @staticmethod
    def not_authorized(domain_name: DomainEnum) -> dict:
        return {
            "model": NotAuthorizedResponse,
            "description": f"User in domain {domain_name} is not authorized",
        }

    @staticmethod
    def forbidden(domain_name: DomainEnum) -> dict:
        return {
            "model": ForbiddenResponse,
            "description": f"Method in domain {domain_name} forbidden to access",  # noqa: E501
        }

    @staticmethod
    def invalid_data(domain_name: DomainEnum) -> dict:
        return {
            "model": ValidationErrorResponse,
            "description": f"Invalid data for {domain_name} entity",
        }

    @staticmethod
    def not_found(domain_name: DomainEnum) -> dict:
        return {
            "model": ErrorResponse,
            "description": f"Not found {domain_name} by uuid",
        }

    @staticmethod
    def conflict(domain_name: DomainEnum) -> dict:
        return {
            "model": ErrorResponse,
            "description": f"Conflict for {domain_name} entity",
        }

    @staticmethod
    def health(domain_name: DomainEnum) -> dict:
        return {
            "description": f"{domain_name} server is ready to work",
            "content": {
                "application/octet-stream": {
                    "example": "",
                },
            },
        }


class ForbiddenResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Error: Forbidden",
            },
        },
    )


class NotAuthorizedResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Error: Not Authorized",
            },
        },
    )


class ErrorResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Method: exception description",
            },
        },
    )


class ValidationErrorResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Invalid request",
                "errors": [
                    {
                        "type": "type of error",
                        "msg": "error message",
                        "loc": "error location",
                    },
                ],
            },
        },
    )
