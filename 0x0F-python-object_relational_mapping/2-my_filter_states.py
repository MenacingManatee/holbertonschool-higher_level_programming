#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conc = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    curs = conc.cursor()

    curs.execute("SELECT * FROM states WHERE name='{}'\
ORDER BY states.id;".format(argv[4]))
    data = curs.fetchall()

    for item in data:
        print(item)

    curs.close()
    conc.close()
