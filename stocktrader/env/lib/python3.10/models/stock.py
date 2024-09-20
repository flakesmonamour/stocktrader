from sqlalchemy import Column, Integer, String
from .connection import Base  # Relative import

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String, index=True)

    @classmethod
    def create(cls, session, symbol, name):
        stock = cls(symbol=symbol, name=name)
        session.add(stock)
        session.commit()
        return stock

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def __repr__(self):
        return f"<Stock(symbol={self.symbol}, name={self.name})>"
