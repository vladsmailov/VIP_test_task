from sqlalchemy import select

from src.core.db.models import DecimalNumber
from src.core.exceptions import ObjectNotFoundError

from . import abstract_repository


class DecimalNumberRepository(abstract_repository.AbstractRepository):
    """Репозиторий для работы с моделью DecimalNumber."""

    def __init__(self, session) -> None:
        super().__init__(session, DecimalNumber)

    def by_name(self, name) -> DecimalNumber:
        decimal_number = self._session.execute(
            select(DecimalNumber).where(DecimalNumber.name == name)
            ).scalars().one_or_none()
        if decimal_number:
            return str(decimal_number.id)
        raise ObjectNotFoundError(DecimalNumber, name)
