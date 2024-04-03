from sqlalchemy.sql import func
from sqlalchemy import Column, String, DateTime, ForeignKey
from src.models.settings.base import Base

class Attendees(Base):
    __tablename__= "attendees"
    id = Column(String, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"))
    created_at = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f"Attendees [name={self.name}, email={self.email}, event_id={self.event_id}]"
