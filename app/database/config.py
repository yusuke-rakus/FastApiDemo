from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# class BaseEngine(object):
#     def __init__(self):
#         username = 'root'
#         password = ''
#         hostname = 'localhost'
#         dbname = 'fast_api_sample'
#         url = f'mysql://{username}:{password}@{hostname}/{dbname}?charset=utf8'
#         self.engine = create_engine(url, echo=True)
#
#
# class BaseSession(BaseEngine):
#     def __init__(self):
#         super().__init__()
#         Session = sessionmaker(bind=self.engine)
#         self.session = Session()


username = 'root'
password = ''
hostname = 'localhost'
dbname = 'fast_api_db'
url = f'mysql+pymysql://{username}:{password}@{hostname}/{dbname}?charset=utf8'
engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
