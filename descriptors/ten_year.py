"""
The python descriptor
Ten years old dog
"""


class Ten:
    """This is simple descriptor that always returns 10"""

    def __get__(self, instance, owner):
        return 10


class ModifyTen:
    """You don't have opportunity change attribute"""

    def __get__(self, instance, owner):
        """
        in the self parameter is link to instance of ModifyTen
        (instance of descriptor)

        in the instance parameter is link to instance of class (owner)

        in the owner parameter is link to class of instance
        """
        print(f'This is instance: {instance}')
        print(f'This is owner: {owner}')
        return 10

    def __set__(self, instance, value):
        """
        in the self parameter is link to instance of ModifyTen
        (instance of descriptor)

        in the instance parameter is link to instance

        in the value parameter is link value that set to instance:
        instance.attr = value
        """
        print(f'This is instance: {instance}')
        print(f'This is value: {value}')
        print("HAHAHA LOL, YOU CAN'T CHANGE THIS")


class Dog:

    year = Ten()


class AlwaysTenDog:

    year = ModifyTen()


def modified_year():
    my_dog = Dog()
    print(my_dog.year)
    my_dog.year = 5
    print(my_dog.year)


def unmodified_year():
    my_dog = AlwaysTenDog()
    print(my_dog.year)
    my_dog.year = 5
    print(my_dog.year)


if __name__ == '__main__':
    modified_year()
    unmodified_year()
