from sqlalchemy import (
    Column,
    Integer,
    String,
    )
from ..db import Base


class Athlete(Base):

    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    email = Column(String(500), nullable=False)
    country = Column(String(500))
