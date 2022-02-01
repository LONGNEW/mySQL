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
sql = """
        create table product(
            product_code varchar(20) not null,
            title varchar(200) not null,
            ori_price int,
            discount_price int,
            discount_percent int,
            delivery varchar(2),
            primary key(product_code)
        );
        """
cursor.execute(sql)

# 모든 쿼리를 실행하도록 하는 함수 (데이터를 변환하고, 복원이 불가한 상황으로 가게 됨)
db.commit()
db.close()