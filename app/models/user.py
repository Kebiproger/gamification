from sqlalchemy import Integer, String,Column,DateTime
from ..db import Base

class User(Base):
    __table__="user"

    id = Column(Integer,index=True)
    username = Column(String)
    score = Column(Integer,default=0)
    lvl = Column(Integer,default=1)
    completed_tasks= Column(Integer,default=0)
