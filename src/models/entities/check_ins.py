from sqlalchemy.sql import func
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from src.models.settings.base import Base

class CheckIns(Base):
    __tablename__= "check_ins"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    attendee_id = Column(String, ForeignKey('attendees.id'))

    def __repr__(self):
        return f"CheckIns [id={self.id}, created_at={self.created_at}, attendee_id={self.attendee_id}]"