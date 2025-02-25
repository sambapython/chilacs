def test_update(customer_object):
    act = customer_object.update_customer()
    expected = "updated"
    assert expected==act