import pytest
from invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def mock_value():
    return 5


def test_CanCalcucateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_Rounding(products):
    invoice = Invoice()
    value = invoice.totalImpurePrice(products)
    invoice.roundingImpurePrice(value)
    assert invoice.roundingImpurePrice(value) == 75


def test_coupons(products):
    total_amount = Invoice().totalImpurePrice(products)
    #print(total_amount)
    result = Invoice().coupon('y', total_amount)
    assert result ==  70
