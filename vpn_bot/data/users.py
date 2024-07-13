import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    tg_id = sa.Column(sa.Integer, nullable=False, unique=True)
    username = sa.Column(sa.VARCHAR(256), nullable=True)
    vpn_num = sa.Column(sa.Integer, unique=True, nullable=True) # QA: Может ли это поле быть пустым? 
                                                                 # Теоретически если пользователь не оплатил, то мы лешаем его VPN
                                                                 # а вместе с этим и номера, при этом в БД это пользователь остаётся
                                                                 # так как в будущем он может к нам вернуться
    used = sa.Column(sa.Integer, nullable=False) # QA: Это поле отвечает за колличество использования VPN в месяц?
    payed = sa.Column(sa.Integer, nullable=False) # QA: Что это за поле? Почему тут integer а не boolean?
    is_admin = sa.Column(sa.Boolean, nullable=False, autoincrement="auto", default=False)


