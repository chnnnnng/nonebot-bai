from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
 
DIALCT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "chenyang20010703"
HOST = "172.17.0.1"
PORT = "33306"
DATABASE = "nonebot"
 
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
 
class admin(Base):
    __tablename__ = "admin"
    id = Column(Integer , primary_key=True , autoincrement=True)
    qq = Column(String(50) , nullable=False)
 
Base.metadata.drop_all()
Base.metadata.create_all()