import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from db_models import Location, Person
from api_models import Location as LocationRequestBody
from api_models import Person as PersonRequestBody
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

try:
    engine = create_engine(os.environ.get("DATABASE_URL"))
except Exception as e:
    print("Error connecting to database: ", e)


@app.get("/locations")
def get_locations():
    with Session(engine) as session:
        return session.query(Location).all()


@app.post("/locations")
def add_location(location: LocationRequestBody):
    with Session(engine) as session:
        if (
            session.query(Location)
            .filter(
                Location.continent == location.continent
                and Location.country == location.country
                and Location.subdivision == location.subdivision
                and Location.city == location.city
            )
            .first()
            is not None
        ):
            raise HTTPException(status_code=409, detail="Location already exists")
        new_location = Location(
            continent=location.continent,
            country=location.country,
            subdivision=location.subdivision,
            city=location.city,
        )
        session.add(new_location)
        session.commit()
        return "Added location"


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
        if person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        session.delete(person)
        session.commit()
        return "Deleted person"
