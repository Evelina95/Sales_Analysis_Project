from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from alchemy_credentials import engine

Base = declarative_base()


class ManoProjektas(Base):
    __tablename__ = "ManoProjektas"

    ID = Column(Integer, primary_key=True)
    name = Column("Vardas", String(255))
    lastname = Column("Pavardė", String(255))
    birthdate = Column("Gimimo data", Date)
    occupation = Column("Pareigos", String(255))
    salary = Column("Atlyginimas", Float)
    startdate = Column("Įsidarbinimo data", DateTime)

    def __init__(self, name, lastname, birthdate, occupation, salary, startdate):

        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.occupation = occupation
        self.salary = salary
        self.startdate = startdate

    def __repr__(self):
        return f"{self.ID} {self.name} {self.lastname} - {self.birthdate} {self.occupation} {self.salary}: {self.startdate}"


Base.metadata.create_all(engine)

