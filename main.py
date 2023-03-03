import csv
class Item:

    items = []
    item_discount = 0
    csv_name = []
    csv_price = []
    csv_value = []

    def __init__(self, item_name='', item_price=0, item_value=0, currency=''):
        """
        Получение информации о товаре
        :param item_name: Наименование товара
        :param item_price: Цена за 1 единицу
        :param item_value: Количество
        :param currency: Валюта(любая)
        """
        self._item_name = item_name
        self.item_price = item_price
        self.item_value = item_value
        self.currency = currency
        Item.items.append(self)
        if self.len_item_name_check(self._item_name):
            self.len_item_name_error(self._item_name)

    @property
    def item_name(self):
        return self._item_name

    #Если честно, я не совсем понял как это вообще работает)) Я что то написал, а почему оно работает я хз)
    @item_name.setter
    def item_name(self, item_name):
        if self.len_item_name_check(item_name):
             self.len_item_name_error(item_name)
        self._item_name = item_name

    def discount_price(self):
        """
        Функция расчета скидок на товар
        :return:
        """
        try:
            x = self.item_price/100*Item.item_discount
            x = self.item_price-x
            return f'С учетом скидки, стоимость {self._item_name.lower()} составляет: {x} {self.currency}'

        except Exception:
            return f'Ошибка ввода информации'

    def total_price(self):
        """
        Функция вывода общей стоимости товара на складе
        :return: Выводит стоимость товара на складе
        """
        try:
            return f"Общая стоимость {self._item_name} на складе: {float(self.item_price * self.item_value)} {self.currency}"

        except Exception:
            return f'Ошибка ввода информации'

    def len_item_name_check(self, item_name, max_len=10):
        """
        Функция проверки на максимальную длинну названия товара
        :param item_name: Название товара
        :param max_len: Максимальная длинна
        :return: Проверка на превышение максимальной длинны
        """
        return len(item_name) > max_len

    def len_item_name_error(self, name):
        """
        Функция ошибки
        :return: Возвращает ошибку
        """
        raise Exception(f'Длинна названия товара {name} не должна превышать 10 символов!')

    def csv_items_load(self):

        with open('items.csv', newline='') as csv_items:
            csv_reader = csv.reader(csv_items)
            for items_csv in csv_reader:
                #Пропускаем первую строку
                if 'name' in items_csv:
                    continue
                self.csv_name.append(items_csv[0])
                for i in self.csv_name:
                    if len(i) > 10:
                        self.len_item_name_error(i)
                self.csv_price.append(items_csv[1])
                self.csv_value.append(items_csv[2])
                self.items.append(f'Название: {items_csv[0]}, цена: {items_csv[1]}, количество: {items_csv[2]}')
            return 'Items loaded' #Для теста

    @staticmethod
    def is_integer(numeric):
        return isinstance(numeric, int)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._item_name}, {self.item_price}, {self.item_value}")'

    def __str__(self):
        return f'{self._item_name}'

    def __add__(self, other):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.item_value + other.item_value
        else:
            raise Exception(f'Не возможно сложить. Попробуйте Phone и Item!')

class Phone(Item):

    def __init__(self, item_name, item_price, item_value, sim_cards, currency=''):
        super().__init__(item_name, item_price, item_value, currency)
        self.sim_cards = sim_cards
        self.sim_cards_error()

    def sim_cards_error(self):
        if self.sim_cards <= 0:
            raise Exception(f'Количество слотов для сим-карт не может быть меньше 1')

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._item_name}, ' \
               f'{self.item_price}, {self.item_value}, ' \
               f'{self.sim_cards}, {self.currency}")'

class TestItem(Item):
    """
    Тестовый класс для проверки сложения между Item и другими классами
    Имея наследование от Item, передается __add__, пришлось добавить его сюда, чтобы изменить его параметры
    При сложении с Phone или Item - возвращает None
    """
    def __add__(self, other):
        pass


if __name__ == '__main__':

    item = Item('Телефон', 10000, 5)
    phone = Phone('iPhone 14', 100000, 7, 1, 'руб')
    test_item = TestItem('Test', 1, 27, 'RUB')
    print(phone)
    print(repr(phone))
    print(item+phone)
    print(test_item+item)
    print(test_item+phone)



