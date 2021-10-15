from sqlalchemy import Column, VARCHAR, INTEGER
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(VARCHAR(4), primary_key=True)
    name = Column(VARCHAR(30))
    age = Column(INTEGER)
    email = Column(VARCHAR(50))

    def __str__(self):
        return f"\n{self.id}\n{self.name}\n{self.age}\n{self.email}"
