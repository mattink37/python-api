from typing import List
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Location(Base):
    __tablename__ = "logged_locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    continent: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    subdivision: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Location(id={self.id!r}, continent={self.continent!r}, country={self.country!r}, subdivision={self.subdivision!r}, city={self.city!r})"


class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.email!r})"
