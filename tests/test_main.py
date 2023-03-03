import pytest
from main import Item
from main import TestItem
from main import Phone


def test_add_method_with_test_item():
    item1 = Phone('Test1', 10, 5, 1, 'USD')
    item2 = Item('Test2', 20, 10, 'EUR')
    result = item1 + item2
    assert result == 15


def test_item_name_length():
    with pytest.raises(Exception):
        TestItem('ЭТО НОВЫЙ ТЕЛЕФОН', 10, 5, 'USD')

def test_class_sum():
    item1 = Item('Test1', 10, 5, 'USD')
    item2 = Phone('Test2', 10, 5, 1, 'USD')
    item3 = TestItem('Test3', 10, 12, 'RUB')
    test_otvet = item1+item2
    test_otvet2 = item2+item3
    assert test_otvet == 10
    assert test_otvet2 == None


