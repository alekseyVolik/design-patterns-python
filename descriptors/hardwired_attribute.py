class HardwiredPrintedAge:
    """Hardwired _age attribute"""

    def __set__(self, instance, value):
        print(f'Set age to object with value={value}')
        instance._age = value

    def __get__(self, instance, owner):
        print('Get age from object')
        return instance._age


class PrintedAge:
    """
    __set_name__ is method that solve issue
    hardwired attribute
    """

    def __set_name__(self, owner, name):
        """
        The method used to inform for which variable name was used
        """
        print('call __str_name__ method')
        self.public_attribute = name
        self.private_attribute = f'_{name}'

    def __set__(self, instance, value):
        print('call __set__ method')
        setattr(instance, self.private_attribute, value)

    def __get__(self, instance, owner):
        print('call __get__ method')
        value = getattr(instance, self.private_attribute)
        return value


class AgeCat:

    age = PrintedAge()


class HardwiredAgeCat:

    age = HardwiredPrintedAge()


def hardwired_attr_issue():
    """
    Private name _age is hardwired in the HardwiredPrintedAge
    class descriptor
    """
    my_cat = HardwiredAgeCat()
    my_cat.age = 7
    print(my_cat.age)


def solve_hardwired_issue():
    """
    The descriptor set value to private attribute with
    help __set_name__ method
    """
    my_cat = AgeCat()
    my_cat.age = 101
    print(my_cat.age)


if __name__ == '__main__':
    hardwired_attr_issue()
    solve_hardwired_issue()
