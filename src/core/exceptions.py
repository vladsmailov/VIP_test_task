from http import HTTPStatus

from src.core.db.database import Base as DatabaseModel


class ApplicationError(Exception):
    """Собственное исключение для бизнес-логики приложения."""

    detail: str = \
        "Какая-то неопознанная ошибка. Мы её обязательно опознаем и исправим!"


class NotFoundError(ApplicationError):
    status_code: HTTPStatus = HTTPStatus.NOT_FOUND


class ObjectNotFoundError(NotFoundError):
    """Ошибка, пробрасываемая при отсутствии искомого объекта в БД."""
    def __init__(self, model: DatabaseModel, object_name: str):
        self.detail = \
            "Объект '{}' с именем '{}' не найден".format(
                model.__name__, object_name
            )
