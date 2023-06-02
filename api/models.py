from sqlalchemy import Column, Integer, String
from api.database import Base


class AudienceModel(Base):
    __tablename__='audience_attributes'
    id=Column(Integer,primary_key=True,nullable=False)
    country=Column(String(30),nullable=False)
    name=Column(String(140),unique=True,nullable=False)
    label=Column(String(450),nullable=False)
    description=Column(String(234),nullable=False)

class AudienceValuesModel(Base):
    __tablename__='audience_attributes_values'
    id=Column(Integer,primary_key=True,nullable=False)
    audience_value=Column(String(40),nullable=False)
    audience_label=Column(String(345),nullable=False)
    audience_description=Column(String(234),nullable=False)
