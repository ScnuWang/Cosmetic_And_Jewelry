from sqlalchemy import Column,Integer,String,DECIMAL,create_engine,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from models import Cj_Model

Base = declarative_base()



# 插入中文会报错，需要在数据库名称后面添加?charset=utf8
engine = create_engine("mysql+pymysql://root:admin@localhost/data?charset=utf8", echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
product = Cj_Model.Cj_Brand(brand_name='Swarosvki',update_time=datetime.now())
session = DBSession()
session.add(product)
session.commit()
session.close()