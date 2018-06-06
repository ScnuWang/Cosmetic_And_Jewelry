from sqlalchemy import Column,Integer,String,DECIMAL,create_engine,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'cj_product_test'
    id = Column(Integer,primary_key=True,autoincrement=True)
    original_id = Column(String(255))
    product_name = Column(String(255))
    def __repr__(self):
        return "<Product(id='%d', original_id='%s', product_name='%s')>" % (self.id, self.original_id, self.product_name)

# 插入中文会报错，需要在数据库名称后面添加?charset=utf8
engine = create_engine("mysql+pymysql://root:admin@localhost/data?charset=utf8", echo=True)
Product.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
product = Product(original_id='432143',product_name='施华洛世奇')
session = DBSession()
session.add(product)
session.commit()
session.close()