import csv


class Item:
    instances = []
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # validate
        assert price >= 0, f"price {price} is not greater or equal to zero"
        # assign
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.instances.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        # context manager used to facilitate proper handling of resources
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
