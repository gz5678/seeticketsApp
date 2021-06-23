from eventsStore.feeCalculator import _calculate_service_fee


def test_allow_zero_service_fee():
    fee = _calculate_service_fee(15, 0, 2)
    assert fee == 0
