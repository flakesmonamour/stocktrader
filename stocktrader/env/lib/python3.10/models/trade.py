# models/trade.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    trader_id = Column(Integer, ForeignKey('traders.id'))  # Foreign key to Trader
    stock_id = Column(Integer, ForeignKey('stocks.id'))    # Assuming you have a Stock model
    amount = Column(Integer)
    price = Column(Float)

    trader = relationship('Trader', back_populates='trades')  # Relationship with Trader

    @classmethod
    def create(cls, session, trader_id, stock_id, amount, price):
        trade = cls(trader_id=trader_id, stock_id=stock_id, amount=amount, price=price)
        session.add(trade)
        session.commit()
        return trade

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def __repr__(self):
        return f"<Trade(trader_id={self.trader_id}, stock_id={self.stock_id}, amount={self.amount}, price={self.price})>"
