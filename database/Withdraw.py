from .db_base import Base
from sqlalchemy import Column, Integer, Float, Boolean, DATE, VARCHAR
import datetime

datetime.date.today()

class Withdraw(Base):
    __tablename__ = "withdraws"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(VARCHAR(50), nullable=False)
    money = Column(Float, default=0)
    create_date = Column(DATE, default=datetime.date.today())
    status = Column(Boolean, default=False)

    def __init__(self, user_id, money):
        self.user_id = user_id
        self.money = money

