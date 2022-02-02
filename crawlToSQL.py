import pymysql

f = open("login.txt", "r")
host, port, user, passwd, db, charset = f.readline().split()
port = int(port)
f.close()

db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = db.cursor()

sql = \
f"""
create table items(
    item_code varchar(20) not null primary key,
    title varchar(20) not null,
    ori_price int not null,
    dis_price int not null,
    discount_percent int not null,
    provider varchar(100)
);
"""

cursor.execute(sql)

sql = \
f"""
create table ranking(
    num int auto_increment not null primary key,
    main_category varchar(50) not null,
    sub_category varchar(50) not null,
    item_ranking tinyint unsigned not null,
    item_code varchar(20) not null,
    foreign key (item_code) references items(item_code)
);
"""

cursor.execute(sql)

db.commit()
db.close()
