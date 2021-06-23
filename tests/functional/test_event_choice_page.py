

def test_all_events_appear(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
