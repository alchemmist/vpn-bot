import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class WGConfig(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "wg_configs"

    id = sa.Column(sa.Integer, primary_key=True)
    used_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False) 
    config_file_path = sa.Column(sa.VARCHAR(256), nullable=False, unique=True)
    
    config_owner = relationship("User")

