#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import MetaData
    from sys import argv
    engine = create_engine('mysql+mysqldb://'+argv[1]+':'+argv[2] +
                           '@localhost:3306/'+argv[3])
    metadata = MetaData()
    conc = engine.connect()
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State).\
        filter(City.state_id == State.id).\
            order_by(City.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    session.close()
