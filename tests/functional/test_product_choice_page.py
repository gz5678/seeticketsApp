import sqlalchemy
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
        data={"1": 2, "2": 3, "currency": "USD", "event_service_fee": 5},
        follow_redirects=True
    )
    assert b'45 USD' in response.data


def test_fee_is_calculated_correctly_when_no_product_fee(test_client, init_database):
    events = Events.query.all()
    for event in events:
        data = {"currency": event.service_fee_currency, "event_service_fee": event.service_fee_amount}
        fee_sum = 0
        for product in event.products:
            if product.service_fee_amount or product.service_fee_amount == 0:
                fee_sum += 3 * product.service_fee_amount
            else:
                fee_sum += 3 * event.service_fee_amount
            data[str(product.id)] = 3
        response = test_client.post(
            '/chooseProducts',
            data=data,
            follow_redirects=True
        )

        assert bytes('{} {}'.format(fee_sum, event.service_fee_currency), encoding='utf-8') in response.data


def test_when_zero_quantity_then_get_zero_fee(test_client, init_database):
    response = test_client.post(
        '/chooseProducts',
        data={"1": 0, "2": 0, "currency": "USD", "event_service_fee": 5},
        follow_redirects=True
    )
    assert b'0 USD' in response.data
