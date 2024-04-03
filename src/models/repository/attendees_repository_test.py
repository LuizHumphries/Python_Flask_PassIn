import pytest
from src.models.settings.connection import db_connection_handler
from src.models.repository.attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Not necessary")
def test_insert_attendees():
    event_id = 'my-uuid-test'
    attendees = {
        "uuid": "my-uuid-attendees_1",
        "name": "Attendees_1",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendees(attendees)
    print(response)

def test_get_attendees_badge_by_id():
    attendees_id = "my-uuid-attendees_1"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendees_badge_by_id(attendees_id=attendees_id)
    print(response)