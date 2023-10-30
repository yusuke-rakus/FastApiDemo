from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class BaseEngine(object):

    def __init__(self):
        username = 'demo'
        password = 'password'
        hostname = 'localhost'
        dbname = 'demo'
        url = f'mysql+pymysql://{username}:{password}@{hostname}/{dbname}?charset=utf8'
        self.engine = create_engine(url, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=BaseEngine().engine)
Base = declarative_base()
