import csv
class Item:
    items = []
    item_discount = 0

    def __init__(self, item_name='', item_price=0, item_value=0, currency=''):
        """
        Получение информации о товаре
        :param item_name: Наименование товара
        :param item_price: Цена за 1 единицу
        :param item_value: Количество
        :param currency: Валюта(любая)
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_value = item_value
        self.currency = currency
        Item.items.append(self)
        if self.len_item_name_check(self.item_name):
            self.len_item_name_error(self.item_name)
    @property
    def name(self):
        return self._name

    #Если честно, я не совсем понял как это вообще работает)) Я что то написал, а почему оно работает я хз)
    @name.setter
    def name(self, value):
        if self.len_item_name_check(value):
            self.len_item_name_error(value)
        self._name = value

    def discount_price(self):
        """
        Функция расчета скидок на товар
        :return:
        """

        try:
            x = self.item_price/100*Item.item_discount
            x = self.item_price-x
            return f'С учетом скидки, стоимость {self.item_name.lower()} составляет: {x} {self.currency}'

        except Exception:
            return f'Ошибка ввода информации'

    def total_price(self):
        """
        Функция вывода общей стоимости товара на складе
        :return: Выводит стоимость товара на складе
        """
        try:
            return f"Общая стоимость {self.item_name} на складе: {float(self.item_price * self.item_value)} {self.currency}"

        except Exception:
            return f'Ошибка ввода информации'

    def len_item_name_check(self, name, max_len=10):
        """
        Функция проверки на максимальную длинну названия товара
        :param name: Название товара
        :param max_len: Максимальная длинна
        :return: Проверка на превышение максимальной длинны
        """
        return len(name) > max_len

    def len_item_name_error(self, name):
        """
        Функция ошибки
        :return: Возвращает ошибку
        """
        raise Exception(f'Длинна названия товара {name} не должна превышать 10 символов!')

class CsvItems:

    all_items = []

    def __init__(self):
        """
        self.name - Хранит названия товаров
        self.price - Хранит стоимость товара за 1 единицу
        self.value - Хранит количество товара на складе
        """
        self.name = []
        self.price = []
        self.value = []

        with open('items.csv', newline='') as csv_items:
            csv_reader = csv.reader(csv_items)
            for items in csv_reader:
                #Пропускаем первую строку
                if 'name' in items:
                    continue
                self.name.append(items[0])
                self.price.append(items[1])
                self.value.append(items[2])
                self.all_items.append(f'Название: {items[0]}, цена: {items[1]}, количество: {items[2]}')

    def is_integer(self, numeric):
        return isinstance(numeric, int)

if __name__ == '__main__':

    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфонyyytytyy'
    print(item.name)

    #item.name = 'СуперСмартфон'

    csv_items = CsvItems()

    print(len(csv_items.all_items))
    print(csv_items.name[0])
    print(csv_items.is_integer(5))
    print(csv_items.is_integer(5.0))



