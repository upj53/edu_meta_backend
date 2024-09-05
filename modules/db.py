from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

config = dotenv_values('.env')

user_name = config['DB_USER_NAME']
user_pwd = config['DB_USER_PWD']
db_host = config['DB_HOST']
db_name = config['DB_NAME']

'''
# default
engine = create_engine("mysql://scott:tiger@localhost/foo")

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")

# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")
'''

DATABASE = f'mysql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8'

ENGINE = create_engine(
  DATABASE,
  echo=True
)

session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
  )
)

Base = declarative_base()
Base.query = session.query_property()

def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()