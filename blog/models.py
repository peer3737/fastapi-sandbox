from .database import Base
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Blog(Base):
    __tablename__ = 'blog'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)
    # Correct way to define a ForeignKey with Mapped and mapped_column
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=True, default=None)

    creator: Mapped["User"] = relationship(back_populates="blogs")


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    # Correct way to define a relationship with Mapped
    blogs: Mapped[List["Blog"]] = relationship(back_populates="creator")
