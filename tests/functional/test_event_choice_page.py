from eventsStore.feeCalculator import NO_EVENT_ERROR_MESSAGE


def test_all_events_appear(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Tomorrowland' in response.data
    assert b'Glastonbury' in response.data
    assert b'Coachella' in response.data


def test_when_url_with_non_existent_event_then_we_get_an_error_flash(test_client, init_database):
    response = test_client.get('/chooseProducts?event=nonExistent', follow_redirects=True)
    assert b'div class="flash"' in response.data
    assert bytes(NO_EVENT_ERROR_MESSAGE, encoding='utf-8')
