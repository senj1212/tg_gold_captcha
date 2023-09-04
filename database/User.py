from sqlalchemy import Column, Integer, VARCHAR, Float, Boolean
from .db_base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(VARCHAR(50), unique=True, nullable=False)
    balance = Column(Float, default=0)
    worked = Column(Boolean, default=False)
    last_captcha = Column(VARCHAR(20), default="")
    wallet = Column(VARCHAR(20), default="")

    def __init__(self, user_id):
        self.user_id = user_id

