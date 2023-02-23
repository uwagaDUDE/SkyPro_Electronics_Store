import pytest
import main

def test_main():

    assert main.Item('Ноутбук', 10000, 2, 'руб').discount_price() == 'С учетом скидки, стоимость ноутбук составляет: 10000.0 руб'
    assert main.Item('Ноутбук', 10000, 2, 'руб').total_price() == 'Общая стоимость Ноутбук на складе: 20000.0 руб'
    assert main.Item('Ноутбук', 'Test', 2, 'руб').discount_price() == 'Ошибка ввода информации'
    assert main.Item('Ноутбук', 'Test', 2, 'руб').total_price() == 'Ошибка ввода информации'
    assert main.Item().is_integer(99) == True
    assert main.Item().is_integer(25.1) == False
    assert main.Item().csv_items_load() == 'Items loaded'
    assert main.Item().csv_name[1] == 'Ноутбук'
    assert main.Item().csv_price[1] == '1000'
    assert main.Item().csv_value[2] == '5'
    assert main.Item().len_item_name_check('Test', max_len=3) == True
    assert main.Item().len_item_name_check('Test', max_len=10) == False
    assert len(main.Item().csv_name) == 5
