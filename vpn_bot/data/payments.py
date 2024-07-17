import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class Payment(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "payments"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    date = sa.Column(sa.DateTime, nullable=False)

    payer = relationship("User")

