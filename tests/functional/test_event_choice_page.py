from eventsStore.feeCalculator import NO_EVENT_ERROR_MESSAGE, NO_EVENTS_IN_DATABASE_MESSAGE
from eventsStore.models import Events


def test_all_events_appear(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Tomorrowland' in response.data
    assert b'Glastonbury' in response.data
    assert b'Coachella' in response.data


def test_when_url_with_non_existent_event_then_we_get_an_error_flash(test_client, init_database):
    response = test_client.get('/chooseProducts?event=nonExistent', follow_redirects=True)
    data = response.get_data(as_text=True)
    assert NO_EVENT_ERROR_MESSAGE in data


def test_when_no_events_in_database_then_present_message(test_client):
    response = test_client.get('/')
    data = response.get_data(as_text=True)
    assert NO_EVENTS_IN_DATABASE_MESSAGE in data
