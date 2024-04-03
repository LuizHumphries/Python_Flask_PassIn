from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import NoResultFound, IntegrityError


class AttendeesRepository:

    def insert_attendees(self, attendees_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendees = Attendees(
                    id=attendees_info.get("uuid"),
                    name=attendees_info.get("name"),
                    email=attendees_info.get("email"),             
                    event_id=attendees_info.get("event_id")       
                )
                database.session.add(attendees)
                database.session.commit()
                return attendees_info
            except IntegrityError:
                raise Exception("Attendees already in database")
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_attendees_badge_by_id(self, attendees_id: str):
        with db_connection_handler as database:
            try:
                attendees = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id == attendees_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        )
                        .one()
                )
                return attendees
            except NoResultFound:
                return None
            
