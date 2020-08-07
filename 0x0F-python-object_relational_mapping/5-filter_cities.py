#!/usr/bin/python3
'''lists all cities in state from the database hbtn_0e_4_usa,
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
    cmds = ""
    if argv[4] is not None:
        cmds = argv[4].split(';')
        cmds = argv[4].strip("'")

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

    res = []
    for c, s in session.query(cities, states).\
        filter(cities.state_id == states.id, states.name == "{}".format(cmds)
               ).order_by(cities.id):
        res.append(c.name)

    print(", ".join(res))
