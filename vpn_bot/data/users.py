import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    tg_id = sa.Column(sa.Integer, nullable=False, unique=True)
    username = sa.Column(sa.VARCHAR(256), nullable=True)
    used = sa.Column(sa.Boolean, nullable=False, autoincrement="auto", default=False)
    is_admin = sa.Column(sa.Boolean, nullable=False, autoincrement="auto", default=False)
    blocked = sa.Column(sa.Boolean, nullable=False, autoincrement="auto", default=False)
    


