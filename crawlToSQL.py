import pymysql
import requests
from bs4 import BeautifulSoup

def connect_db():
    f = open("login.txt", "r")
    host, port, user, passwd, db, charset = f.readline().split()
    port = int(port)
    f.close()
    db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

    return db

def excute_db(db, sql):
    cursor = db.cursor()

    sql = \
    f"""
    """

    cursor.execute(sql)

def close_db(db):
    db.commit()
    db.close()


res = requests.get("http://corners.gmarket.co.kr/Bestsellers")
soup = BeautifulSoup(res.content, "html.parser")

categories = soup.select("#categoryTabG li a")
# bs4에서 링크를 가져오는 법, 내부 텍스트를 가져오는 방법.
for item in categories:
    print(item["href"], item.get_text())
