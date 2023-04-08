from sqlalchemy import  Column, String, Integer, CHAR
from extention import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    firstname = Column('firstname', String(16))
    lastname = Column('lastname', String(16))
    gender = Column('gender', CHAR(1))
    age = Column('age', Integer)

    def __init__(self, first_name, last_name, gender, age):
        self.firstname = first_name
        self.lastname = last_name
        self.gender = gender
        self.age =  age

    def __repr__(self):
        return f"({self.firstname}) ({self.lastname})"
    
    def get_persorn_email(self):
        return f" {self.firstname}.{self.lastname}@company.com"
      