from typing import List

from fastapi import Depends

from src.core.db.models import Product
from src.core.db.repository.decimal_number_repository import \
    DecimalNumberRepository
from src.core.db.repository.product_repository import ProductRepository


class ProductService:
    """Вспомогательный класс для Product.

    Внутри реализованы методы для формирования итогового
    отчета.
    """

    def __init__(
        self,
        product_repository: ProductRepository = Depends(),
        decimal_number_repository: DecimalNumberRepository = Depends()
    ) -> None:
        self.__product_repository = product_repository
        self.__decimal_number_repository = decimal_number_repository

    def get_by_status(self, start):
        """
        Метод получения Product.

        При отсутствии значения атрибута updated_at
        и значении status == in_progress.
        """
        return self.__product_repository.by_status(start)

    def get_by_start_end_decimal_number(self, start, end, name) -> Product:
        """
        Метод получения Product по трем значениям.

        (start, end, decimal_number)."""
        decimal_number_id = self.__decimal_number_repository.by_name(name)
        product = self.__product_repository.by_start_end_decimal_number(
            start, end, decimal_number_id
        )
        return product

    def get_without_decimal_number(self, start, end) -> List[Product]:
        """
        Метод получения списка объектов Product без указания decimal_number.
        """
        return self.__product_repository.by_start_end(start, end)
