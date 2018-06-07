from sqlalchemy import Column, Integer, String, DECIMAL, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:admin@localhost/data?charset=utf8", echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

# 产品表
class Cj_Product(Base):
    __tablename__ = 'cj_product'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    original_id = Column('original_id', String, comment="原始编号")
    brand_id = Column('brand_id', Integer, comment="品牌编号")
    location_id = Column('location_id', Integer, comment="销售地点编号")
    product_name = Column('product_name', String(255), comment="产品名称")
    product_price = Column('product_price', DECIMAL(16, 2), comment="产品名称")
    original_currency = Column('original_currency', String(255), comment="原始币种")
    product_url = Column('product_url', String(255), comment="产品详情地址")
    product_image = Column('product_image', String(512), comment="产品图片地址")
    product_thumbnail = Column('product_thumbnail', String(512), comment="产品缩略图地址")
    old_price = Column('old_price', DECIMAL(16, 2), comment="原始价格")
    product_name_zh = Column('product_name_zh', String(512), comment="中文别名")
    cny_product_price = Column('cny_product_price', DECIMAL(16, 2), comment="产品人民币价格")
    cny_exchange_rate = Column('cny_exchange_rate', DECIMAL(16, 2), comment="对人民币汇率")
    product_status_id = Column('product_status_id', Integer, comment="产品状态")
    category_id = Column('category_id', Integer, comment="产品分类")
    update_time = Column('update_time', DateTime, comment='更新时间')


# 品牌表
class Cj_Brand(Base):
    __tablename__ = 'cj_brand'
    __table_args__ = {"useexisting": True}
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    brand_name = Column('brand_name', String(255), comment="品牌名称")
    update_time = Column('update_time', DateTime, comment='更新时间')


# 分类表
class Cj_Category(Base):
    __tablename__ = 'cj_category'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    category_name_zh = Column('category_name_zh', String(255), comment="中文名称")
    category_name_en = Column('category_name_en', String(255), comment="英文名称")
    update_time = Column('update_time', DateTime, comment='更新时间')


# 汇率表
class Cj_Currency(Base):
    __tablename__ = 'cj_currency'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    currency = Column('currency', String(255), comment="币种简写")
    exchange_rate_cny = Column('exchange_rate_cny', String(255), comment="对换人民币汇率")
    update_time = Column('update_time', DateTime, comment='更新时间')


# 销售地点表
class Cj_Location(Base):
    __tablename__ = 'cj_location'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sales_location = Column('sales_location', String(255), comment="销售地点")
    update_time = Column('update_time', DateTime, comment='更新时间')

# 产品状态表
class Cj_Product_Status(Base):
    __tablename__ = 'cj_product_status'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product_status = Column('product_status', String(255), comment="销售地点")
    update_time = Column('update_time', DateTime, comment='更新时间')
