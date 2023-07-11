from fastapi import FastAPI
from sqlalchemy import create_engine
from db_models import Person
from api_models import Person as PersonRequestBody
from sqlalchemy.orm import Session

app = FastAPI()
engine = create_engine("postgresql://localhost/matt")


@app.get("/people")
def get_people():
    with Session(engine) as session:
        return session.query(Person).all()


@app.post("/people")
def add_person(person: PersonRequestBody):
    with Session(engine) as session:
        new_person = Person(name=person.name, email=person.email)
        session.add(new_person)
        session.commit()
        return "Added person"


@app.delete("/people/{person_id}")
def delete_person(person_id: int):
    with Session(engine) as session:
        person = session.query(Person).filter(Person.id == person_id).first()
        session.delete(person)
        session.commit()
        return "Deleted person"
