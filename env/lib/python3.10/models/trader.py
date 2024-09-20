from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .connection import Base

class Trader(Base):
    __tablename__ = 'traders'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    trades = relationship('Trade', back_populates='trader')

    @classmethod
    def create(cls, session, name):
        trader = cls(name=name)
        session.add(trader)
        session.commit()
        return trader

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def __repr__(self):
        return f"<Trader(name={self.name})>"
