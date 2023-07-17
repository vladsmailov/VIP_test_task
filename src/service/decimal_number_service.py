import uuid

from fastapi import Depends

from src.core.db.repository.decimal_number_repository import \
    DecimalNumberRepository


class ProductService:
    """
    Вспомогательный класс для Product.

    Внутри реализованы методы для формирования итогового
    отчета.
    """

    def __init__(
        self,
        decimal_number_repository: DecimalNumberRepository = Depends()
    ) -> None:
        self.__decimal_number_repository = decimal_number_repository

    def get_by_name(self, name) -> uuid:
        """Получаем DecimalNumber.id по имени."""
        decimal_number = self.__decimal_number_repository.by_name(name)
        return decimal_number.id
