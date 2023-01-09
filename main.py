from item import Item
from phone import Phone

Item.instantiate_from_csv()

item1 = Item("newPhone",400,4)
item1.apply_increment(0.2)
item1.apply_discount()
print(Item.instances)

