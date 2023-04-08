from sqlalchemy import  Column,ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from extention import Base


class Things(Base):
    __tablename__ = 'thing'

    id = Column(Integer, primary_key=True)
    description = Column('description', String(100))
    owner_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship('Person', foreign_keys='Things.owner_id')
    

    def __init__(self, description, owner):
        self.description = description
        self.owner = owner
    
    def __repr__(self):
        return f"({self.description}) ownde by ({self.owner})"
