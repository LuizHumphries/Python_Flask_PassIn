from src.models.repository.event_repository import EventRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
import uuid


class EventHandler:
    def __init__(self) -> None:
        self.__event_repository = EventRepository()
    
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__event_repository.insert_event(body)

        return HttpResponse(
            body={"event_id": body["uuid"]},
            status_code= 200
        )
    
    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__event_repository.get_event_by_id(event_id)
        if not event:
            raise HttpNotFoundError("Event not found!")
        
        event_attendes_count = self.__event_repository.count_event_attendees(event_id)

        return HttpResponse(
            body={"event": {
                "id": event.id,
                "title": event.title,
                "details": event.details,
                "slug": event.slug,
                "maximum_attendees": event.maximum_attendees,
                "attendees_amount": event_attendes_count["attendees_amout"]
            }},
            status_code=200
        )