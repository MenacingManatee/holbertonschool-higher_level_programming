#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


import sqlalchemy
import MySQLdb
from model_state import *
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, session, conc

from sys import argv

class City(Base):
    '''Table defining cities'''
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
