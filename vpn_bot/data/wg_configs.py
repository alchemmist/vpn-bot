import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin

from .db import SqlAlchemyBase


class WGConfig(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "wg_configs"

    id = sa.Column(sa.Integer, primary_key=True)
    num = sa.Column(sa.Integer, autoincrement="auto", unique=True) # QA: Это тот vpn_num который мы прописывали в users? Т
                                                                   # Тогда почему не сделать relation на таблицу users?
    config_file_path = sa.Column(sa.VARCHAR(256), nullable=False, unique=True)
    

