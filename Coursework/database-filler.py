#  Database Filler

import pyodbc
from faker import Faker

fake = Faker(["en_UK"])


def fillCust():
    cnxn = dbCon()
    cursor = cnxn.cursor()
    cursor.execute("delete from Customer")
    for i in range(20):
        name = fake.name().split(" ")
        firstname = name[len(name) - 2]
        surname = name[len(name) - 1]
        phone = fake.phone_number()
        delete = "() +"
        for j in range(len(delete)):
            phone = phone.replace(f"{delete[j]}", "")
        email = fake.email()
        username = f"{firstname[0:3]}{surname[0:3]}{randint(10,99)}"
        cursor.execute(
            f"insert into Customer values('{i}','{username}','{username}','{firstname}','{surname}','{phone[-10:]}','{email}')"
        )
    cursor.commit()


def fillStaff():
    cnxn = dbCon()
    cursor = cnxn.cursor()
    cursor.execute("delete from Staff")
    for i in range(5):
        name = fake.name().split(" ")
        firstname = name[len(name) - 2]
        surname = name[len(name) - 1]
        phone = fake.phone_number()
        delete = "() +"
        for j in range(len(delete)):
            phone = phone.replace(f"{delete[j]}", "")
        email = fake.email()
        username = f"{firstname[0:3]}{surname[0:3]}{randint(10,99)}"
        cursor.execute(
            f"insert into Staff values('{i}','{username}','{username}','{firstname}','{surname}','{phone[-10:]}','{email}')"
        )
    cursor.commit()


def fillTable():
    cnxn = dbCon()
    cursor = cnxn.cursor()
    cursor.execute("delete from [Table]")
    for i in range(10):
        capacity = 2 * randint(1, 5)
        cursor.execute(f"insert into [Table] values ('{i}','{capacity}')")
    cursor.commit()


if __name__ == "__main__":
    fillCust()
    fillStaff()
    fillTable()
