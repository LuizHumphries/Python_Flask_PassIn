from sqlalchemy import Column, String, Integer
from src.models.settings.base import Base

class Events(Base):
    __tablename__= "events"
    id = Column(String(200), nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)
