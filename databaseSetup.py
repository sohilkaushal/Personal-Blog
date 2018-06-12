import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    uID = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(10000), nullable=False)
    dateOfRegisteration = Column(DateTime, default=datetime.datetime.now)


class Post(Base):
    postID= Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1000))
    description = Column(String(10000))
    owner = Column(Integer, ForeignKey('user.uID'))

engine = create_engine('sqlite:///blogDatabase.db')
Base.metadata.create_all(engine)
