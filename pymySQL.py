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
    select * from students;
"""

# pandas를 통해 DB 커넥션을 사용해서 쿼리 던지기
# csv 파일 생성 함수 (파일 이름, 구분자, 인덱스 유무, 인코딩)
df = pd.read_sql(sql, db)
df.to_csv('students.csv', sep=',', index=False, encoding='utf-8')

db.commit()
db.close()