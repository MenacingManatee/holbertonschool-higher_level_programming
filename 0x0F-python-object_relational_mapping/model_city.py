#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


if __name__ == "__main__":
    import sqlalchemy
    import MySQLdb
    from model_state import *
    from sqlalchemy import MetaData
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sys import argv
    engine = create_engine('mysql+mysqldb://'+argv[1]+':'+argv[2] +
                           '@localhost:3306/'+argv[3])
    conc = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()


    class City(Base):
        '''Table defining cities'''
        __tablename__ = 'cities'

        id = Column(Integer, autoincrement=True, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('State.id'))
