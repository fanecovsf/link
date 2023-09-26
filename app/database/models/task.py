import sqlalchemy as sql
import sqlalchemy.orm as orm
from sqlalchemy.orm import DeclarativeBase
from typing import Optional


class TaskLog(DeclarativeBase):


    __tablename__ = 'tb_tasks_log'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

