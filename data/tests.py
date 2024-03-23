# Класс с описанием таблицы новостей

import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Tests(SqlAlchemyBase):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    quest = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    a_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    a_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    a_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    a_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    r_a = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ball = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    theme_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("theme.id"))
    theme = orm.relationship('Theme')
