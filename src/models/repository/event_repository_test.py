import pytest
from src.models.settings.connection import db_connection_handler
from src.models.repository.event_repository import EventRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register into database")
def test_insert_event():
    event = {
        "uuid": "my-uuid-test-3",
        "title": "My Title",
        "slug": "slug-data-3",
        "maximum_attendees": 20
    }
    event_repository = EventRepository()
    response = event_repository.insert_event(event)
    print(response)

#@pytest.mark.skip(reason="Not necessary")
def test_get_event_by_id():
    event_id = "my-uuid-test-26565"
    event_repository = EventRepository()
    response = event_repository.get_event_by_id(event_id=event_id)
    print(response)
    
