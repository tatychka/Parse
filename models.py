from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
# Задекларировали
Base = declarative_base()
№
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=False)
    write_id = Column(Integer, ForeignKey('writer.id'))

class Writer(Base):
    __tablename__ = 'writer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=False)
    url = Column(String, nullable=False, unique=True)