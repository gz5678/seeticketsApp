from eventsStore.models import Events, Products


def test_deleting_event_deletes_the_related_products(test_db):
    event1 = Events(name="Tomorrowland", service_fee_amount=5, service_fee_currency="USD")
    product1 = Products(name="VIP", service_fee_amount=15, service_fee_currency="USD")
    product2 = Products(name="Weekend", service_fee_amount=10, service_fee_currency="USD")
    event1.products.extend([product1, product2])
    test_db.session.add(event1)
    test_db.session.commit()

    event = Events.query.all()[-1]
    test_db.session.delete(event)
    test_db.session.commit()
    assert len(Events.query.all()) == 0
    assert len(Products.query.all()) == 0
