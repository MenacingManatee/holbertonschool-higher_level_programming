#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


if __name__ == "__main__":
    import sqlalchemy
    from relationship_state import Base, State
    from relationship_city import City
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

    newstate = State(name="California")
    s_id = session.query(State.id).filter(
        State.name == "California").first()
    newcity = City(name="San Francisco", state_id=s_id)

    session.add(newstate)
    session.add(newcity)
    session.commit()

    session.close()
