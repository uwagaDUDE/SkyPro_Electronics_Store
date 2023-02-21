import csv
class Item:
    items = []
    item_discount = 0


    def __init__(self, item_name='', item_price=0, item_value=0, currency=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_value = item_value
        self.currency = currency
        Item.items.append(self)

    @property
    def name(self):
        return self._name

    #Если честно, я не совсем понял как это вообще работает)) Я что то написал, а почему оно работает я хз)
    @name.setter
    def name(self, value):
        if self.len_item_name_check(value):
            self.len_item_name_error()
        self._name = value

    def discount_price(self):

        try:

            x = self.item_price/100*Item.item_discount
            x = self.item_price-x

            return f'С учетом скидки, стоимость {self.item_name.lower()} составляет: {x} {self.currency}'

        except KeyError:
            return f'Ошибка ввода информации'

    def total_price(self):
        try:
            return f"Общая стоимость {self.item_name} на складе: {float(self.item_price * self.item_value)} {self.currency}"
        except KeyError:
            return f'Ошибка ввода информации'

    def len_item_name_check(self, name):
        return len(name) > 10

    def len_item_name_error(self):
        raise Exception(f'Длинна названия товара не должна превышать 10 символов!')

class CsvItems:

    all_items = []

    def __init__(self):
        with open('items.csv', newline='') as csv_items:
            csv_reader = csv.reader(csv_items)
            for items in csv_reader:
                self.name=items[0]
                self.price=items[1]
                self.value=items[2]
                self.all_items.append(f'Название: {self.name}, цена: {self.price}, количество: {self.value}')

print(len(CsvItems().all_items)-1)



