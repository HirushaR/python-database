# python-database

#### requirment 
* ``` pip install sqlalchemy```
*  ``` pip install pymysql```

### Object-relational mapping (ORM) 
Object-relational mapping (ORM) is a way to align programming code with database structures. ORM uses metadata descriptors to create a layer between the programming language and a relational database. It thus connects object-oriented program (OOP) code with the database and simplifies the interaction between relational databases and OOP languages.
### SQLALCHEMY 
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.


#### DB connections

we can use create_engine class in SQLAlchemy  to create a connection between python app and relational database.

```python
#import create engine from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#connection string
url = 'mysql+pymysql://root:password@localhost/database'
#connection 
engine = create_engine(url=url, echo=True)
#connection pass to session 
Session = sessionmaker(bind=engine)
#we can use session to create database access  
session= Session()
```

### Create Table in database from python 

to create table in database from python we need create a class for that table. in that class, it should contain variables for all the comlumn in the table

```python
from sqlalchemy import  Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

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
```
```__tablename__``` we can assign name for table
now when we ran the file it if the tabel person is not created it will create new table with those column. 


#### CREATE RECORD 

```python
# create object from Person class
p1 = Person("Jhon", "doe", 'M', 30)
# add this object to session in database
session.add(p1)
# added this object to databse - create record
session.commit()
```
in this it will run 
```sql
INSERT INTO person(firstname, lastname, gender, age) VALUES ("Jhon", "doe", "M", 30);
```