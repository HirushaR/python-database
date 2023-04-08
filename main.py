from person import Person
from things import Things
from extention import Base, engine, session


Base.metadata.create_all(bind=engine)


#  insert data into person table
# p1 = Person("Jhon", "doe", 'M', 30)
# p2 = Person("Same", "lin", 'S', 20)
# p3 = Person("Neil", "EM", 'M', 35)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

#retrive data from person table

# result =  session.query(Person).filter(Person.firstname == 'Hirusha')
# result =  session.query(Person).filter(Person.firstname.in_(["Same", "Neil"]))
# result =  session.query(Person).filter(Person.firstname.like("%Sa%"))
# for r in result:
#     print(r.get_persorn_email())



# insert data into thins table 
# person_1 =  session.query(Person).filter(Person.firstname == 'Hirusha').one()
# t1 = Things('car', person_1)
# session.add(t1)
# session.commit()


#retrive data from Things table
# result = session.query(Things).one()

#result = session.query(Things).filter(Things.owner_id == Person.id).filter(Person.firstname == 'Hirusha').one()
# for r in result:
#
#      print(r)

#update
#result.description = 'van'

#session.add(result)
#session.commit()
#print(result)

#delete
# result = session.query(Person).filter(Person.firstname == 'Neil').one()

# session.delete(result)

# # commit (or flush)
# session.commit()