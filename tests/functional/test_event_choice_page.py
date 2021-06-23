

def test_all_events_appear(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Tomorrowland' in response.data
    assert b'Glastonbury' in response.data
    assert b'Coachella' in response.data
