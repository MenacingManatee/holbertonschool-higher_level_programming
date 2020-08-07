#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_4_usa,
in ascending order by city id'''


if __name__ == "__main__":
    import sqlalchemy
    import MySQLdb
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sys import argv
    engine = create_engine('mysql+mysqldb://'+argv[1]+':'+argv[2]+'\
@localhost:3306/'+argv[3])
    conc = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

    class states(Base):
        '''Table defining states'''
        __tablename__ = 'states'

        id = Column(Integer, autoincrement=True, primary_key=True)
        name = Column(String(256))

    class cities(Base):
        '''Table defining cities'''
        __tablename__ = 'cities'

        id = Column(Integer, autoincrement=True, primary_key=True)
        state_id = Column(Integer)
        name = Column(String(256))

    for c, s in session.query(cities, states).\
        filter(cities.state_id == states.id).\
            order_by(cities.id):
        print("({}, '{}', '{}')".format(c.id, c.name, s.name))
