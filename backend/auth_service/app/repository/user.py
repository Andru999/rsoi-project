from uuid import UUID

from dto.user import UserFilterDto, UserUpdateDto
from model.user import UserModel
from sqlalchemy.orm import Query, Session
from utils.addons import hash_password, ilike_search


class UserRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    async def get_all(
        self,
        filter_dto: UserFilterDto,
        offset: int = 0,
        limit: int = 100,
    ) -> tuple[list[UserModel], int]:
        query = self._db.query(UserModel)
        query = await self.__filter_users(query, filter_dto)
        total = query.count()

        return query.offset(offset).limit(limit).all(), total

    async def get_by_uuid(self, uuid: UUID) -> UserModel | None:
        return self._db.query(UserModel).filter(UserModel.uuid == uuid).first()

    async def get_by_id(self, id: int) -> UserModel | None:  # noqa: A002
        return self._db.query(UserModel).filter(UserModel.id == id).first()

    async def create(self, model: UserModel) -> UserModel | None:
        if type(model.password) is str:
            model.password = hash_password(
                password=model.password,
            )

        try:
            self._db.add(model)
            self._db.commit()
            self._db.refresh(model)
        except:
            return None

        return model

    async def update(
        self,
        model: UserModel,
        model_update: UserUpdateDto,
    ) -> UserModel | None:
        model_updated_fileds = model_update.model_dump(exclude_unset=True)
        for key, value in model_updated_fileds.items():
            setattr(model, key, value)

        return await self.create(model)

    async def delete(self, model: UserModel) -> UserModel:
        self._db.delete(model)
        self._db.commit()

        return model

    async def __filter_users(
        self,
        query: Query[UserModel],
        filter_dto: UserFilterDto,
    ) -> Query[UserModel]:
        if filter_dto.login:
            query = query.filter(
                UserModel.login.ilike(ilike_search(filter_dto.login)),
            )
        if filter_dto.lastname:
            query = query.filter(
                UserModel.lastname.ilike(ilike_search(filter_dto.lastname)),
            )
        if filter_dto.firstname:
            query = query.filter(
                UserModel.firstname.ilike(ilike_search(filter_dto.firstname)),
            )
        if filter_dto.email:
            query = query.filter(
                UserModel.email.ilike(ilike_search(filter_dto.email)),
            )
        if filter_dto.phone:
            query = query.filter(
                UserModel.phone.ilike(ilike_search(filter_dto.phone)),
            )
        if filter_dto.role:
            query = query.filter(UserModel.role == filter_dto.role)

        return query
