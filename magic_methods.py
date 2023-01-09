##double underscore aka dundr

##__str__ if overriden inside a class that will be used for str conversion

class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer

    def __str__(self):
        if self.integer == 4:
            return 'Four'
        return str(self.integer)

    def __repr__(self):
        return f'CustomizedInteger({self.integer})'

#alternatively __repr__ can also be used. First print searches for __str__ if that is not avaialble
# checks __repr__ to display the object in formal manner for ease of object creation later
#__str__ is expected to make string more presenatble

int1 = CustomizedInteger(4)
int2 = CustomizedInteger(2)
print(int1)
print(int2)