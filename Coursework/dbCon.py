import pyodbc
from config import DBCSTRING


def dbCon():
    try:
        cs = DBCSTRING
        print("connecting")
        cnxn = pyodbc.connect(cs)
        print("Connected!")
        return cnxn
    except pyodbc.DatabaseError as err:
        print(err)
        return err


if __name__ == "__main__":
    dbCon()
