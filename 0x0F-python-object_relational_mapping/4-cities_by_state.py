#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conc = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    curs = conc.cursor()

    curs.execute("SELECT cities.id, cities.name, states.name\
 FROM states\
 LEFT JOIN cities\
 ON cities.state_id=states.id\
 ORDER BY cities.id")
    data = curs.fetchall()

    for item in data:
        print(item)

    curs.close()
    conc.close()
