from sqlalchemy import Column, String, Integer
from src.models.settings.base import Base

class Events(Base):
    __tablename__= "events"
    id = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}, slug={self.slug}]"
