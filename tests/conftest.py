import pytest
from eventsStore import create_app, db
from eventsStore.models import Events, Products


@pytest.fixture
def test_db():
    app = create_app(test_config='test_config.py')
    with app.app_context():
        yield db
        db.drop_all()


@pytest.fixture(scope='module')
def test_client():
    app = create_app(test_config='test_config.py')

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture
def init_database(test_client):
    event1 = Events(name="Tomorrowland", service_fee_amount=5, service_fee_currency="USD")
    event2 = Events(name="Glastonbury", service_fee_amount=10, service_fee_currency="GBP")
    event3 = Events(name="Coachella", service_fee_amount=15, service_fee_currency="USD")

    product1 = Products(name="VIP", service_fee_amount=15, service_fee_currency="USD")
    product2 = Products(name="Weekend", service_fee_amount=5, service_fee_currency="USD")
    product3 = Products(name="VIP", service_fee_currency="GBP")
    product4 = Products(name="Weekend", service_fee_amount=15, service_fee_currency="GBP")
    product5 = Products(name="Day", service_fee_currency="USD")
    product6 = Products(name="Weekend", service_fee_amount=5, service_fee_currency="USD")

    event1.products.extend([product1, product2])
    event2.products.extend([product3, product4])
    event3.products.extend([product5, product6])

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)

    db.session.commit()

    yield

    db.drop_all()
    db.create_all()
