from sqlalchemy import Column, String, Integer, Float

from swagger_server.orm.BaseORM import BaseORM


class DistanceORM(BaseORM):
    __tablename__ = 'distance'

    id = Column(Integer(), primary_key=True)
    s1 = Column(String(255))
    s2 = Column(String(255))
    d = Column(Float())
