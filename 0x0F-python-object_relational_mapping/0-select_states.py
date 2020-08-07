#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


import sqlalchemy
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
engine = create_engine('mysql+mysqldb://'+argv[1]+':'+argv[2]+'\
@localhost:3306/'+argv[3])
conc = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(engine)
Base = declarative_base()
metadata.reflect()


class states(Base):
    '''Table defining states'''
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256))


for id, name in session.query(states.id, states.name).order_by(states.id):
    print("({}, '{}')".format(id, name))
