import enum
import uuid

from sqlalchemy import (DATETIME, VARCHAR, Column, Enum, ForeignKey,
                        Integer)
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.database import Base


class ProductStatusTypeENUM(str, enum.Enum):
    """Класс ProductStatusTypeENUM для поля Product.status."""
    EFFECTIVE = "годен"
    DEFECT = "не годен"
    IN_PROGRESS = "в работе"


class Product(Base):
    """Класс Product."""
    __tablename__ = "Product"

    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=True)
    deleted_at = Column(DATETIME, nullable=True, default=None)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pid = Column(UUID, nullable=True, default=None)
    sequence_number = Column(Integer, nullable=False)
    status = Column(Enum(ProductStatusTypeENUM))
    order_in = Column(UUID, nullable=True, default=None)
    decimal_number_id = Column(
        UUID, ForeignKey("Decimal_number.id"), nullable=True
    )
    output_number = Column(VARCHAR, nullable=True, default=None)
    status_info = Column(VARCHAR, nullable=True)


class DecimalNumber(Base):
    """Класс DecimalNumber."""
    __tablename__ = "Decimal_number"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR, nullable=False)
