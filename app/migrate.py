from .database.config import BaseEngine
from .models.models import Base


class Migration(object):
    def __init__(self):
        self.e = BaseEngine().engine

    def users(self):
        Base.metadata.create_all(self.e)


if __name__ == '__main__':
    Migration().users()
