class Item:
    items = []
    item_discount = 0


    def __init__(self, item_name='', item_price=0, item_value=0, currency=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_value = item_value
        self.currency = currency
        Item.items.append(self)

    def discount_price(self):

        try:
            x = self.item_price/100*Item.item_discount
            x = self.item_price-x
            return f'С учетом скидки, стоимость {self.item_name.lower()} составляет: {x} {self.currency}'
        except Exception:
            return f'Ошибка ввода информации'

    def total_price(self):
        try:
            return f"Общая стоимость {self.item_name} на складе: {float(self.item_price * self.item_value)} {self.currency}"
        except Exception:
            return f'Ошибка ввода информации'

Item('Ноутбук', 10000, 2, 'руб').discount_price()