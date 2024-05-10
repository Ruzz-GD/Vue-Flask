from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_tbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=True)

    def __repr__(self):
        return f'<GmailAuthentication(id={self.id}, username={self.username})>'

