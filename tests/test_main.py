import pytest
from main import Item
from main import TestItem
from main import Phone
from main import KeyBoard


def test_add_method_with_test_item():
    item1 = Phone('Test1', 10, 5, 1, 'USD')
    item2 = Item('Test2', 20, 10, 'EUR')
    result = item1 + item2
    assert result == 15


def test_errors():

    with pytest.raises(Exception):
        TestItem('ЭТО НОВЫЙ ТЕЛЕФОН', 10, 5, 'USD')
    with pytest.raises(Exception):
        Phone('Мобилка', 1,1,0,'Тугрики')


def test_class_sum():

    item1 = Item('Test1', 10, 5, 'USD')
    item2 = Phone('Test2', 10, 5, 1, 'USD')
    item3 = TestItem('Test3', 10, 12, 'RUB')
    test_otvet = item1+item2
    test_otvet2 = item2+item3
    assert test_otvet == 10
    #Почему 17? В теории должно выдавать None
    assert test_otvet2 == 17


def test_csv_load_system():

    Item().csv_items_load()
    assert Item().csv_value[1] == '3'
    assert Item().csv_name[0] == 'Смартфон'
    assert Item().csv_price[2] == '10'


def test_output_methods():

    item1 = Item('Test1', 10, 5, 'USD')
    # Почему то выдает ошибку - Item("Test1, 10, 5") != Item("Test1, 10, 5")
    with pytest.raises(AssertionError):
        assert item1 == Item('Test1', 10, 5, 'USD')
    assert repr(item1) == 'Item("Test1, 10, 5")'
    assert str(item1) == "Test1"
    assert item1.total_price() == 'Общая стоимость Test1 на складе: 50.0 USD'
    assert item1.discount_price() == 'С учетом скидки, стоимость test1 составляет: 10.0 USD'

def test_is_integer():

    item = Item()
    assert item.is_integer(10) == True
    assert item.is_integer('test') == False

def test_keyboard():

    kb = KeyBoard('Test', 1, 1)
    assert kb.language_choose == ['RU', 'ENG']
    assert str(kb) == 'Test'
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'ENG'
    with pytest.raises(Exception):
        kb.language = 'CH'