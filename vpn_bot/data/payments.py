import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class Payment(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "payments"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    date = sa.Column(sa.DateTime, nullable=False)
    moth = sa.Column(sa.Integer, nullable=False) # QA: Что это за поле? Зачем оно нужно,
                                                 # если выше мы уже сохранили всю дату со временм

    payer = relationship("User")
