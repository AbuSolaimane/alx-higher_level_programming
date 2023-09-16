#!/usr/bin/python3
"""
this is a module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

Base = declarative_base()


class State(Base):
    """
    this is a class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
