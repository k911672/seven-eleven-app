from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, inspect

engine = create_engine("postgresql://bsmxicbdjonioa:4c2007e168e50fde082a9de86e96b7f87a788a4c7c2a0fac14715aa09f332cbb@ec2-100-24-169-249.compute-1.amazonaws.com:5432/da270e89tu8m9c")
Base = declarative_base()


class Products(Base):
    __tablename__ = "products"  # テーブル名を指定
    id = Column(Integer, primary_key=True)
    category = Column(String(255))
    name = Column(String(255))
    price = Column(Integer)
    image = Column(String(255))


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    inspector = inspect(engine)
    columns = inspector.get_columns("products")
    print(columns)
