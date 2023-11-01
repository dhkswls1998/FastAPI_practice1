from sqlalchemy import Column, Integer, String, DateTime
from app.database.sqlite import Base
from datetime import datetime

class User(Base):
    __tablename__ = "UserID"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    age = Column(Integer)
    login_time = Column(DateTime, default=datetime.utcnow)