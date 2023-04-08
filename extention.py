from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mysql+pymysql://root:password@localhost/test_sls'
Base = declarative_base()


engine = create_engine(url=url, echo=True)


Session = sessionmaker(bind=engine)
session= Session()




