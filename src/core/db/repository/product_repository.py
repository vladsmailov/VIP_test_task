from typing import List

from sqlalchemy import select

from src.core.db.models import Product

from . import abstract_repository


class ProductRepository(abstract_repository.AbstractRepository):
    """Репозиторий для работы с моделью Product."""

    def __init__(self, session) -> None:
        super().__init__(session, Product)

    def by_status(self, start) -> List[Product]:
        """Получаем объекты по дате создания и статусу."""
        return self._session.execute(
            select(Product).
            where(
                Product.updated_at is None,
                Product.status == 'IN_PROGRESS',
                Product.created_at >= start
            )
        ).all()

    def by_start_end_decimal_number(
            self, start, end, decimal_number_id
    ) -> Product:
        """Получаем объекты по трем параметрам."""
        product = self._session.execute(
            select(Product)
            .where(
                Product.decimal_number_id == decimal_number_id,
                Product.created_at >= start,
                Product.updated_at <= end
            )
        ).scalars().all()
        return product

    def by_start_end(self, start, end) -> List[Product]:
        """Получаем объекты по двум параметра (начало, конец)"""
        return self._session.execute(
            select(Product).
            where(
                Product.created_at >= start,
                Product.updated_at <= end
            )
        ).all()
