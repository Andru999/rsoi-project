from pydantic import BaseModel, ConfigDict


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
