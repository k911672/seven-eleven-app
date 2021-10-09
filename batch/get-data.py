# # 弁当
# url = "https://www.sej.co.jp/products/a/cat/010020010000000/"
# # カフェ
# url = "https://www.sej.co.jp/products/a/sevencafe/"
# # サラダ
# url = "https://www.sej.co.jp/products/a/cat/040020010000000/"

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

SEARCH_LIST = [{
    'category': "弁当",
    'url': "https://www.sej.co.jp/products/a/cat/010020010000000/"
}, {
    'category': "カフェ",
    'url': "https://www.sej.co.jp/products/a/sevencafe/"
}, {
    'category': "サラダ",
    'url': "https://www.sej.co.jp/products/a/cat/040020010000000/"
},

]

engine = create_engine(
    "postgresql://bsmxicbdjonioa:4c2007e168e50fde082a9de86e96b7f87a788a4c7c2a0fac14715aa09f332cbb@ec2-100-24-169-249.compute-1.amazonaws.com:5432/da270e89tu8m9c")
Base = declarative_base()

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()


class Products(Base):
    __tablename__ = "products"  # テーブル名を指定
    id = Column(Integer, primary_key=True)
    category = Column(String(255))
    name = Column(String(255))
    price = Column(Integer)
    image = Column(String(255))


def get_data():
    ssl._create_default_https_context = ssl._create_unverified_context

    for target in SEARCH_LIST:
        for page in range(1, 20):
            try:
                html = urlopen(f'{target["url"]}{page}/l15/')
                soup = BeautifulSoup(html, "html.parser")

                products_elms = soup.find('div', {'class': 'flex_wrap'})
                if products_elms:
                    products = products_elms.find_all('div', {'class': "list_inner"})
                    print(len(products))

                    for product in products:
                        url = product.find('img').get('data-original')
                        name = product.find('div', {'class': 'item_ttl'}).get_text()
                        price = int(
                            product.find('div', {'class': 'item_price'}).get_text().split('税込')[1].split('円')[0].split(
                                '.')[
                                0])
                        obj = Products(category=target['category'], name=name, price=price, image=url)
                        session.add(obj)
                        print(url, name, price, target['category'])
                    session.commit()
            except Exception:
                continue


if __name__ == "__main__":
    get_data()
