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

    unf_res = session.query(State.id, State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(State.id, City.id).all()

    fil_res = []
    for i in unf_res:
        if i not in fil_res:
            fil_res.append(i)
    print(fil_res)
    tmp = ""
    for tup in fil_res:
        if tmp != tup[1]:
            print("{}: {}".format(tup[0], tup[1]))
            tmp = tup[1]
        print("\t{}: {}".format(tup[2], tup[3]))
