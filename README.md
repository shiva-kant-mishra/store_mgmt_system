# store_mgmt_system
practice python oops


->print( f"some string {var_name}" )

-> a new variable can be attached to class instance (item1) explicitly called Instance Atrribute
    item1.has_color = False

-> explicitly define argument types 
    def __init__(self, name: str, price : float, quantity=0):
        pass
    **for float both int and float values will be accepted**

-> use assert for validations, with custom error message for AssertionError
    assert price >= 0 , f"Price {price} is not greater or equal to zero"
    assert quantity >= 0 , f"Quantity {quantity} is not greater or equal to zero" 

-> Python first checks for Instance Variables , if not available then searches in Class attributes
-> to check all attributes to class or instance
    class_name.__dict__
    instance_name.__dict__

-> to represent an object in readable form
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"         ##to print Item('Phone', 100, 1)

-> isinstance(num, float) ---- to check type of num
-> num.is_integer()  ---- return true/false

## when to use class methods (@classmethod) and when to use static methods (@staticmethod)  

                    1st Argument (convention)   Purpose?
-> regular method   instance AKA self           fn specific to that instance0
-> class method     class AKA cls               class specific fn i.e. to update a class attribute (act as alternate constructors)
-> static method    no mandatory arg            perform a standalone fn , not necessarily class specific

-> self.__class__.__name__ gives name of the class whose instance is used

-> @property // Property Decorator is used to create Read-only attribute i.e can be assigned only once
    @property
    def name(self):
        option 1: return self.name          --> completely read-only attribute no assignment or reassignment even inside class
        option 2: return self._name         --> value can be changed from inside the class ,BUT from outside can be accessed as class_name._name
        option 3: return self.__name        --> value cannot be reassigned from outside the class

-> to make a method private add __ to its name
    def __connect(self):
        pass
    this method can't be accessed from outside