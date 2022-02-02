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

def get_provider():
    ret =
    return ret

def get_items(html, name, sub_name):
    ret = []
    items = html.select("div.best-list")

    # HTML에서 동일한 클래스를 가진 다른 2개가 존재함.
    # 원하는 정보를 골라서 사용하는 방식.
    # 중요! get_text()와 같은 함수는 결국 그 객체가 존재해야 함.
    # 존재하지 않으면 당연히 에러가 발생하게 됨.
    for idx, item in enumerate(items[1].select("li")):
        title = item.select_one("a.itemname").get_text()
        ori_price = item.select_one("div.o-price").get_text()

        # 여러 태그들을 확인한 후에 모든 태그에 맞는 코드 생성.
        dis_price = item.select_one("div.s-price strong span").get_text()
        dis_percent = item.select_one("div.s-price em").get_text()


def sub(link, name):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "html.parser")

    categories = soup.select("div.navi.group a")
    for item in categories:
        print(item.get_text())

res = requests.get("http://corners.gmarket.co.kr/Bestsellers")
soup = BeautifulSoup(res.content, "html.parser")

categories = soup.select("#categoryTabG li a")
for item in categories:
    sub("http://corners.gmarket.co.kr" + item["href"], item.get_text())

