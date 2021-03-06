#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State

class City(Base):
    '''Table defining cities'''
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id, ondelete='CASCADE'))
