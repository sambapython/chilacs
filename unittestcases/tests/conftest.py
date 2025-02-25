import pytest
from app import Customer
@pytest.fixture
def customer_object():
    return Customer(1,"cust1")