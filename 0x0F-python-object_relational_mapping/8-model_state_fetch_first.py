#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa,
in ascending order by state id'''


if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sys import argv
    engine = create_engine('mysql+mysqldb://'+argv[1]+':'+argv[2] +
                           '@localhost:3306/'+argv[3])
    conc = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    count = 0
    res = ""

    try:
        for id, name in session.query(State.id, State.name).order_by(
                State.id).first():
            if count == 0:
                res = "{}: {}".format(id, name)
                count += 1
        print(res)
    except TypeError:
        print("Nothing")
