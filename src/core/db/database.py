from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.core.db.configuration import (DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT,
                                       DB_USER)

SQLALCHEMY_DATABASE_URL = \
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


meta = MetaData(bind=engine)
MetaData.reflect(meta)

Base = declarative_base()
