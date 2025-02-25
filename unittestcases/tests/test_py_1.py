import pytest
from unittest.mock import patch, MagicMock
from app import add, Customer

class DummyResponse:
    def json(self):
        return {"staus_code":200,"data":{}}

@patch('app.call_api_create')
def test_1create(mock_call_api, customer_object):
    mock_call_api.return_value = MagicMock(json=lambda x=0:{"staus_code":200,"data":{}})
    act = customer_object.create_customer()
    expected = "created"
    assert expected==act

@pytest.mark.parametrize("input1,input2,expected",
[(1,2,3),
(1,2.5,3.5),
(1,"2.5", None)
]
)
def test_add(input1, input2, expected):
    actual = add(input1,input2)
    assert actual==expected