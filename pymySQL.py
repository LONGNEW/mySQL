import pymysql

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = db.cursor()

sql = f"""
    update product set 
    title="원피스 가디건 코디전", 
    ori_price=33000, 
    discount_price=9900, 
    discount_percent=70
    where product_code="215673141"
"""
cursor.execute(sql)

# # fetchall()을 통해 출력된 모든 결과들을 가져옴.
# ret = cursor.fetchall()
#
# for item in ret:
#     print(*item)

db.commit()
db.close()