from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call inherited class constructor
        super().__init__(
            name, price, quantity
        )

        # validation for brokenphones
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign
        self.broken_phones = broken_phones
