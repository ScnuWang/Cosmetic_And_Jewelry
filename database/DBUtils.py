from sqlalchemy import Table,Column,Integer,String,DateTime,DECIMAL,MetaData,ForeignKey,create_engine


engine = create_engine("mysql+pymysql://root:admin@localhost/data?charset=utf8", echo=True)
metaData = MetaData()
# 在创建之前检查每个表的存在情况，因此可以安全地调用多次
metaData.create_all(engine)
conn = engine.connect()

# 产品表
cj_product = Table('cj_product',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('original_id', String, comment="原始编号"),
    Column('brand_id', Integer, comment="品牌编号"),
    Column('location_id', Integer, comment="销售地点编号"),
    Column('product_name', String(255), comment="产品名称"),
    Column('product_price', DECIMAL(16, 2), comment="产品名称"),
    Column('original_currency', String(255), comment="原始币种"),
    Column('product_url', String(255), comment="产品详情地址"),
    Column('product_image', String(512), comment="产品图片地址"),
    Column('product_thumbnail', String(512), comment="产品缩略图地址"),
    Column('old_price', DECIMAL(16, 2), comment="原始价格"),
    Column('product_name_zh', String(512), comment="中文别名"),
    Column('cny_product_price', DECIMAL(16, 2), comment="产品人民币价格"),
    Column('cny_exchange_rate', DECIMAL(16, 2), comment="对人民币汇率"),
    Column('product_status_id', Integer, comment="产品状态"),
    Column('category_id', Integer, comment="产品分类"),
    Column('update_time', DateTime, comment='更新时间')
)

# 品牌表
cj_brand =  Table('cj_brand',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('brand_name', String(255), comment="品牌名称"),
    Column('update_time', DateTime, comment='更新时间')
)

# 分类表
cj_category = Table('cj_category',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('category_name_zh', String(255), comment="中文名称"),
    Column('category_name_en', String(255), comment="英文名称"),
    Column('update_time', DateTime, comment='更新时间')
)

# 汇率表
cj_currency = Table('cj_currency',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('currency', String(255), comment="币种简写"),
    Column('exchange_rate_cny', String(255), comment="对换人民币汇率"),
    Column('update_time', DateTime, comment='更新时间')
)

# 销售地点表
cj_location = Table('cj_location',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sales_location', String(255), comment="销售地点"),
    Column('update_time', DateTime, comment='更新时间')
)

# 产品状态表
cj_product_status = Table('cj_product_status',metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('product_status', String(255), comment="产品状态"),
    Column('update_time', DateTime, comment='更新时间')
)

