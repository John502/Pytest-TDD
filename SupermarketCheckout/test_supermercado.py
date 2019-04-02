# Can create instance of Checkout classmethod
# Can add item price
# Can add an item
# Can calculate the current total
# Can add multiple items and get correct total
# Can add discount rules
# Can apply discount rules to the total
# Exception is thrown from item added without a price

import pytest
from Checkout import Checkout


@pytest.fixture(autouse=True)
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b",  2)
    return checkout

# Can calculate the current total
def test_CanCalculatetotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1

# Can add multiple items and get correct total
def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

# Can add discount rules
def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

#skips a unit test
# @pytest.mart.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_execption_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")
