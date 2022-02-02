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
    ret = None
    return ret

def get_items(html, name, sub_name):
    ret = []
    items = html.select("div.best-list")

    for idx, item in enumerate(items[1].select("li")):
        temp = dict()
        rank = idx + 1
        title = item.select_one("a.itemname")
        ori_price = item.select_one("div.o-price")
        dis_price = item.select_one("div.s-price strong span")
        dis_percent = item.select_one("div.s-price em")

        if ori_price == None or ori_price.get_text() == "":
            ori_price = dis_price

        if dis_price == None:
            ori_price, dis_price = 0, 0
        else:
            ori_price = ori_price.get_text().replace(",", "").replace("원", "")
            dis_price = dis_price.get_text().replace(",", "").replace("원", "")

        if dis_percent == None or dis_percent.get_text() == "":
            dis_percent = 0
        else:
            dis_percent = dis_percent.get_text().replace("%", "")

        product_link = item.select_one("div.thumb > a").attrs["href"]
        item_code = product_link.split("=")[1].split("&")[0]

        res = requests.get(product_link)
        soup = BeautifulSoup(res.content, "html.parser")
        provider = soup.select_one("div.item-topinfo_headline span.text__seller a")

        if provider == None:
            provider = ""
        else:
            provider = provider.get_text()

        sql = f"""
            insert into ranking
            (main_category, sub_category, item_ranking, item_code) 
            values ('{name}', '{sub_name}', {rank}, '{item_code}');
        """
        print(sql)


def sub(link, name):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "html.parser")

    get_items(soup, name, "ALL")

    categories = soup.select("div.navi.group li > a")
    for item in categories:
        res = requests.get("http://corners.gmarket.co.kr/" + item["href"])
        soup = BeautifulSoup(res.content, "html.parser")

        get_items(soup, name, item.get_text())

db = connect_db()
res = requests.get("http://corners.gmarket.co.kr/Bestsellers")
soup = BeautifulSoup(res.content, "html.parser")

categories = soup.select("#categoryTabG li a")
for item in categories:
    sub("http://corners.gmarket.co.kr" + item["href"], item.get_text())

