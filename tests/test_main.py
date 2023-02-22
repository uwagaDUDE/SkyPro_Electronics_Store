import pytest
import main

def test_main():
    assert main.Item('Ноутбук', 10000, 2, 'руб').discount_price() == 'С учетом скидки, стоимость ноутбук составляет: 10000.0 руб'
    assert main.Item('Ноутбук', 10000, 2, 'руб').total_price() == 'Общая стоимость Ноутбук на складе: 20000.0 руб'
    assert main.Item('Ноутбук', 'Test', 2, 'руб').discount_price() == 'Ошибка ввода информации'
    assert main.Item('Ноутбук', 'Test', 2, 'руб').total_price() == 'Ошибка ввода информации'
    assert main.CsvItems().all_items[0] == 'Название: Смартфон, цена: 100, количество: 1'
    assert main.CsvItems().is_integer(5) == True
    assert main.CsvItems().is_integer(5.0) == False

@pytest.mark.xfail
def failed_test_main():
    assert main.Item('СуперНоутбук123', 10000, 2, 'руб').total_price() == Exception