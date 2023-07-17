import contextlib

from fastapi import FastAPI

from src.core.db.database import SessionLocal, engine
from src.core.db.models import Base
from src.core.db.repository.decimal_number_repository import \
    DecimalNumberRepository
from src.core.db.repository.product_repository import ProductRepository
from src.core.excel_generator.builder import ThreeParametersReport
from src.service.product_service import ProductService

Base.metadata.create_all(bind=engine)

app = FastAPI()


COLUMNS = [
    'Serial_number',
    'Valid',
    'Date',
    'Time',
    'Sensor_name',
    'RM_ID',
    'Operator',
    'UID'
]


def get_data(session, start, end, name):
    """Получаем данные из таблиц Prduct, Decimal_number."""
    if name:
        return [get_by_start_end_decimal_number(start, end, name, session)]
    else:
        return get_by_start_end(start, end, session) \
            + get_by_status(start, session)


def create_report(data, start, end, name):
    """Формируем отчет в excel-файле."""
    report = ThreeParametersReport(COLUMNS)
    workbook = report.create_workbook()
    parsed_data = report.parse_data(data)
    workbook_with_data = report.add_data(workbook, parsed_data, name)
    report.save_to_excel(workbook_with_data, start, end, name)


def get_by_start_end_decimal_number(start, end, name, session):
    """
    Получаем данные из таблицы Product по трем параметрам.

    -start (Product.created_at)
    -end (Updated_at)
    -name (DecimalNumber.name)
    """
    product_repository = ProductRepository(session)
    decimal_number_repository = DecimalNumberRepository(session)
    product_service = ProductService(
        product_repository,
        decimal_number_repository
    )
    return product_service.get_by_start_end_decimal_number(start, end, name)


def get_by_start_end(start, end, session):
    """Получаем данные из таблицы Product по двума параметрам."""
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    return product_service.get_without_decimal_number(start, end)


def get_by_status(start, session):
    """
    Получаем данные из таблицы Product по одному параметру.

    При отсутствии у объекта Product параметра updated_at
    получаем объекты со статусом EFFECTIVE И created_at == start.
    """
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    return product_service.get_by_status(start)


@contextlib.contextmanager
def get_db():
    """Создаем сессию."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    print("--start")
    start = input()
    print("--end")
    end = input()
    print("--deciamal_number(name)")
    name = input()
    with get_db() as session:
        data = get_data(session, start, end, name)
    create_report(data, start, end, name)
