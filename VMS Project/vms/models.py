from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)  # superadmin, branchadmin, supervisor
    branch = Column(String, nullable=True)

class Camera(Base):
    __tablename__ = 'cameras'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    location = Column(String)
    source_name = Column(String)
    added_by = Column(Integer, ForeignKey('users.id'))
    edited_by = Column(Integer, ForeignKey('users.id'), nullable=True)
    added_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship('User', foreign_keys=[added_by])

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(String)
