from sqlalchemy import Column, Integer, String, DateTime, Sequence, REAL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from datetime import datetime
Base = declarative_base()


class Results(Base):
    __tablename__ = 'inference_table'
    index = Column(Integer, primary_key=True, autoincrement=True)
    Sepal_Length = Column(REAL)
    Sepal_Width = Column(REAL)
    Petal_Length = Column(REAL)
    Petal_Width = Column(REAL)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


