from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)

    items = relationship("Item", backref="user")


class Item(Base):
    __tablename__ = 'item'

    item_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
