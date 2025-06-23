from typing import List, Optional
from sqlalchemy import func, DateTime
from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Goal(Base):
    __tablename__ = 'goals'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    task: Mapped[List['Task']] = relationship(back_populates='goal')


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=True)
    created_at  = None
    finished_at = None
    deadline = None
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    goal_id: Mapped[int] = mapped_column(ForeignKey('goals.id'))
    goal: Mapped['Goal'] = relationship(back_populates='task')
