from sqlalchemy import Table,Column,Integer,String,DateTime,DECIMAL,MetaData,ForeignKey
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:admin@localhost/data?charset=utf8", echo=True)
metaData = MetaData()

users = Table('users',metaData,
                Column('id', Integer, primary_key=True),
                Column('name', String(255)),
                Column('fullname', String(255))
        )

addresses = Table(
                'addresses',metaData,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('users.id')),
                Column('email_address', String(255), nullable=False)
)
# 在创建之前检查每个表的存在情况，因此可以安全地调用多次
metaData.create_all(engine)
# 插入一条记录
ins = users.insert().values(name='jason',fullname='jason wang')

conn = engine.connect()
result = conn.execute(ins)
inserted_primary_key = result.inserted_primary_key

# 插入多条记录
conn.execute(addresses.insert(),[{'user_id': 1, 'email_address' : 'jack@yahoo.com'},
   {'user_id': 1, 'email_address' : 'jack@msn.com'},
   {'user_id': 2, 'email_address' : 'www@www.org'},
   {'user_id': 2, 'email_address' : 'wendy@aol.com'},])