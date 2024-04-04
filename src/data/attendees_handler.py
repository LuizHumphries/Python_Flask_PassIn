from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.event_repository import EventRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_conflict import HttpConflictError
import uuid

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__event_repository = EventRepository()
    
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        event_attendes_count = self.__event_repository.count_event_attendees(event_id)
        if (event_attendes_count["attendees_amout"]) and (event_attendes_count["maximum_attendees"] <= event_attendes_count["attendees_amout"]):
            raise HttpConflictError("Event is sold out! Try another one")
        
        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendees(body)
        return HttpResponse(body=None, status_code=201)
        
    
    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendees_badge_by_id(attendee_id)
        if not badge:
            raise HttpNotFoundError("Attendee not found!")  

        return HttpResponse(
            body={"badge": {
                "name": badge.name,
                "email": badge.email,
                "event_title": badge.title
            }},
            status_code=200
        )

    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)

        if not attendees:
            raise HttpNotFoundError("Attendees not found!")
        
        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "check_ins": attendee.checked_in_at,
                    "created_at": attendee.attendees_created_at
                }
            )
        return HttpResponse(
            body={"attendees": formatted_attendees},
            status_code= 200)

        
