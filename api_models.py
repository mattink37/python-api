from pydantic import BaseModel


class Person(BaseModel):
    name: str
    email: str


class Location(BaseModel):
    continent: str
    country: str
    subdivision: str
    city: str
