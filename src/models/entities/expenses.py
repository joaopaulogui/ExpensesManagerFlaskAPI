from sqlalchemy import Column, String, BigInteger, Integer, Date
from src.models.settings.base import Base
import datetime

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self, description: str, type: str, date: str, cost: int):
        self.description = description
        self.type = type
        self.cost = cost

        y, m, d = date.split("-")       
        self.date = datetime.date(int(y), int(m), int(d))

    def __repr__(self):
        return f"Expenses [id={self.id}, description={self.description}, date={self.date} cost={self.cost}]"