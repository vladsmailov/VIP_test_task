import datetime
import uuid

from pydantic import BaseModel


class ProductBase(BaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime
    id: uuid
    pid: uuid
    sequence_number: int
    status: str
    order_in: uuid
    decimal_number_id: uuid
    output_number: str
    status_info: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime
    id: uuid
    pid: uuid
    sequence_number: int
    status: str
    order_in: uuid
    decimal_number_id: uuid
    output_number: str
    status_info: float

    class Config:
        orm_mode = True


class DecimalNumberBase(BaseModel):
    id: uuid
    name: str


class DecimalNumberCreate(DecimalNumberBase):
    pass


class DecimalNumber(DecimalNumberBase):
    id: uuid
    name: str

    class Config:
        orm_mode = True
