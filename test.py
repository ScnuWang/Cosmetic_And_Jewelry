from database.DBUtils import conn,cj_brand,metaData,engine,cj_product
from sqlalchemy.sql import select
from datetime import datetime
# 在创建之前检查每个表的存在情况，因此可以安全地调用多次
# Python间的模块引用不会执行这一句，所以这句代码不能放在DBUtils文件里面
metaData.create_all(engine)
# sql = cj_brand.insert().values(brand_name='Swarosvki',update_time=datetime.now())
# conn.execute(ins)

sql = select([cj_product]).limit(10)
count = 0;
for row in conn.execute(sql):
    count += 1
print(count)