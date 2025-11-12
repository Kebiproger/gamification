from sqlalchemy import Integer, String,Column,DateTime
from ..db import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,index=True,primary_key=True)
    hashed_password = Column(String)
    username = Column(String)
    score = Column(Integer,default=0)
    lvl = Column(Integer,default=1)
    completed_tasks= Column(Integer,default=0)
