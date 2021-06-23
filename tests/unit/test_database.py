from eventsStore.models import Events, Products, association_table


def test_association_between_event_and_product(test_db):
    event1 = Events(name="Tomorrowland", service_fee_amount=5, service_fee_currency="USD")
    product1 = Products(name="VIP", service_fee_amount=15, service_fee_currency="USD")
    event1.products.append(product1)
    test_db.session.add(event1)
    test_db.session.commit()

    associations = test_db.session.query(association_table).all()
    assert len(associations) == 1
    association = associations[-1]
    assert association.event_id == event1.id
    assert association.product_id == product1.id

    eventsFromDatabase = Events.query.all()
    assert len(eventsFromDatabase) == 1
    event = eventsFromDatabase[-1]
    assert len(event.products) == 1
    product = event.products[0]
    assert product.name == product1.name
    assert product.service_fee_amount == product1.service_fee_amount
    assert product.service_fee_currency == product1.service_fee_currency
