import pymysql
import pandas as pd

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = db.cursor()

sql = \
f"""
    delete from usertbl where userid="STJ ";
"""
cursor.execute(sql)

db.commit()
db.close()