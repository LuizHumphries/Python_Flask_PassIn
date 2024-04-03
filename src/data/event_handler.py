from src.models.repository.event_repository import EventRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
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