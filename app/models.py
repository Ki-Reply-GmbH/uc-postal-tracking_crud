from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Package(Base):
    __tablename__ = "packages"

    id = Column(String, primary_key=True, index=True)
    status = Column(String)
    description = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)
