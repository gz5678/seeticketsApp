from eventsStore.models import Events


def test_all_products_appear(test_client, init_database):
    events = Events.query.all()
    for event in events:
        response = test_client.get('/chooseProducts?event={}'.format(event.name), follow_redirects=True)
        for product in event.products:
            assert bytes(product.name, encoding='utf-8') in response.data


def test_fee_is_calculated_correctly(test_client, init_database):

    response = test_client.post(
        '/chooseProducts',
        data={"VIP": 30, "Weekend": 15},
        follow_redirects=True
    )
    assert b'45' in response.data
