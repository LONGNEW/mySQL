import pymysql

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = db.cursor()

# f"" 을 통해 더 편하게 sql 구문을 만들기.
for idx in range(10):
    code = 215673140 + idx
    sql = f"""insert into product 
    values ({code}, "스위트 바니 여름신상", 23000, 6900, 70, "F");
    """
    cursor.execute(sql)

# # fetchall()을 통해 출력된 모든 결과들을 가져옴.
# ret = cursor.fetchall()
#
# for item in ret:
#     print(*item)

db.commit()
db.close()