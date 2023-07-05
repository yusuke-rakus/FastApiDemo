from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseEngine(object):
    def __init__(self):
        username = 'username'
        password = 'password'
        hostname = 'localhost'
        dbname = 'db_name'
        url = f'mysql://{username}:{password}@{hostname}/{dbname}?charset=utf8'
        self.engine = create_engine(url, echo=True)


class BaseSession(BaseEngine):
    def __init__(self):
        super().__init__()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
