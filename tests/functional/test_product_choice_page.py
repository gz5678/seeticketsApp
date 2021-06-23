from eventsStore.models import Events


def test_all_products_appear(test_client, init_database):
    events = Events.query.all()
    for event in events:
        response = test_client.get('/chooseProducts?event={}'.format(event.name), follow_redirects=True)
        for product in event.products:
            assert bytes(product.name, encoding='utf-8') in response

