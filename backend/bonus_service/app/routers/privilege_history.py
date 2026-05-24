from typing import Annotated
from uuid import UUID

from cruds.interfaces.privilege_history import IPrivilegeHistoryCRUD
from cruds.privilege_history import PrivilegeHistoryCRUD
from enums.auth import RoleEnum
from enums.responses import RespPrivilegeHistoryEnum
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import Response
from models.privilege_history import PrivilegeHistoryModel
from schemas.privilege_history import (
    PrivilegeHistory,
    PrivilegeHistoryCreate,
    PrivilegeHistoryFilter,
)
from services.privilege_history import PrivilegeHistoryService
from sqlalchemy.orm import Session
from utils.auth_user import RoleChecker
from utils.database import get_db


def get_privilege_history_crud() -> type[IPrivilegeHistoryCRUD]:
    return PrivilegeHistoryCRUD


router = APIRouter(
    prefix="/privilege_histories",
    tags=["Privilege History REST API operations"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespPrivilegeHistoryEnum.InvalidData.value,  # noqa: E501
        status.HTTP_401_UNAUTHORIZED: RespPrivilegeHistoryEnum.NotAuthorized.value,  # noqa: E501
        status.HTTP_403_FORBIDDEN: RespPrivilegeHistoryEnum.Forbidden.value,
    },
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[PrivilegeHistory],
    responses={
        status.HTTP_200_OK: RespPrivilegeHistoryEnum.GetAll.value,
    },
)
async def get_all_privilege_histories(
    db: Annotated[Session, Depends(get_db)],
    privilegeHistoryCRUD: Annotated[
        IPrivilegeHistoryCRUD,
        Depends(get_privilege_history_crud),
    ],
    privilege_id: Annotated[int | None, Query(ge=1)] = None,
    ticket_uid: UUID | None = None,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> list[PrivilegeHistoryModel]:
    return await PrivilegeHistoryService(
        privilegeHistoryCRUD=privilegeHistoryCRUD,
        db=db,
    ).get_all(
        privilege_history_filter=PrivilegeHistoryFilter(
            privilege_id=privilege_id,
            ticket_uid=ticket_uid,
        ),
    )


@router.get(
    "/{privilege_history_id}/",
    status_code=status.HTTP_200_OK,
    response_model=PrivilegeHistory,
    responses={
        status.HTTP_200_OK: RespPrivilegeHistoryEnum.GetByID.value,
        status.HTTP_404_NOT_FOUND: RespPrivilegeHistoryEnum.NotFound.value,
    },
)
async def get_privilege_history_by_id(
    db: Annotated[Session, Depends(get_db)],
    privilegeHistoryCRUD: Annotated[
        IPrivilegeHistoryCRUD,
        Depends(get_privilege_history_crud),
    ],
    privilege_history_id: int,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> PrivilegeHistoryModel:
    return await PrivilegeHistoryService(
        privilegeHistoryCRUD=privilegeHistoryCRUD,
        db=db,
    ).get_by_id(privilege_history_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        status.HTTP_201_CREATED: RespPrivilegeHistoryEnum.Created.value,
        status.HTTP_409_CONFLICT: RespPrivilegeHistoryEnum.Conflict.value,
    },
)
async def create_new_privilege_history(
    db: Annotated[Session, Depends(get_db)],
    privilegeHistoryCRUD: Annotated[
        IPrivilegeHistoryCRUD,
        Depends(get_privilege_history_crud),
    ],
    privilege_history_create: PrivilegeHistoryCreate,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> Response:
    privilege_history = await PrivilegeHistoryService(
        privilegeHistoryCRUD=privilegeHistoryCRUD,
        db=db,
    ).add(privilege_history_create)

    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "Location": f"/api/v1/privilege_histories/{privilege_history.id}",
        },
    )


@router.delete(
    "/{privilege_history_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespPrivilegeHistoryEnum.Delete.value,
        status.HTTP_404_NOT_FOUND: RespPrivilegeHistoryEnum.NotFound.value,
    },
)
async def remove_privilege_history_by_id(
    db: Annotated[Session, Depends(get_db)],
    privilegeHistoryCRUD: Annotated[
        IPrivilegeHistoryCRUD,
        Depends(get_privilege_history_crud),
    ],
    privilege_history_id: int,
    _: bool = Depends(
        RoleChecker(allowed_roles=[RoleEnum.USER, RoleEnum.MODERATOR]),
    ),
) -> Response:
    await PrivilegeHistoryService(
        privilegeHistoryCRUD=privilegeHistoryCRUD,
        db=db,
    ).delete(privilege_history_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
