#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conc = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    curs = conc.cursor()
    cmd = argv[4].split(';')
    state = cmd[0].strip("'")

    curs.execute("SELECT cities.name\
 FROM cities\
 LEFT JOIN states\
 ON states.id=cities.state_id\
 WHERE states.name='{}'\
    ORDER BY cities.id".format(state))
    data = curs.fetchall()

    res = []
    for item in data:
        res.append(item[0])

    print(", ".join(res))
    curs.close()
    conc.close()
