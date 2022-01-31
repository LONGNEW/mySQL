import pymysql

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

# 특정 DB에 연결하는 과정
db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

# 입력하는 실해창을 가져오는 방식.
# 커서를 통해 입력을 하게 됨.
cursor = db.cursor()
