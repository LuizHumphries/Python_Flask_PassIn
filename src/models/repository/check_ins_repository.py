from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import NoResultFound, IntegrityError
from src.errors.error_types.http_conflict import HttpConflictError


class CheckInRepository:

    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_ins = CheckIns(attendee_id=attendee_id)
                database.session.add(check_ins)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise HttpConflictError("Check in already in database")
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_check_in_by_id(self, check_in_id: int):
        with db_connection_handler as database:
            try:
                check_ins = (
                    database.session
                        .query(CheckIns)
                        .join(Attendees, Attendees.id == CheckIns.attendeeId)
                        .filter(CheckIns.id == check_in_id)
                        .one()
                )
                return check_ins
            except NoResultFound:
                return None
            
