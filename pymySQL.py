import pymysql
import pandas as pd

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = db.cursor()

# 현재 TABLE "bytTbl"에서 userID가 "userTbl"의 아이디를 참조하는 foriegn key로 설정.
# 그럴 경우 추가 되는 데이터의 userID가 "userTbl"에 존재하지 않는 경우 에러가 발생하게 됨.
sql = \
f"""
    INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('STJ', '운동화', '의류', 30, 2);
"""
cursor.execute(sql)

db.commit()
db.close()