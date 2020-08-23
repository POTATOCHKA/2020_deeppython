import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="{1812120101qwertyUIOP}",
    auth_plugin='mysql_native_password',
    database="testdb"
)
mycursor = mydb.cursor()
sentence = "students"
a = 'name'
b = 'age'
"""
SQLformula = f"INSERT INTO {sentence} ({a}, {b}) VALUES (%s, %s)"
student1 = ("sss",33)

mycursor.execute(SQLformula, student1)

mydb.commit()"""
c = 1000
popka = 'sss'
"""sql = f"UPDATE {sentence} SET {b} = {c} WHERE {a} = '{popka}'"
mycursor.execute(sql)
mydb.commit()"""
"""
sql = f"DELETE FROM {sentence} WHERE {a} = '{popka}'"
mycursor.execute(sql)
mydb.commit()"""

"""sql = f"DROP TABLE IF EXISTS {sentence}"
mycursor.execute(sql)
mydb.commit()"""

"""mycursor.execute(f"CREATE TABLE {sentence} ({a} VARCHAR(255), {b} INTEGER(10))")"""