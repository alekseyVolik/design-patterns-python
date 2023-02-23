"""
Create a few simple metaclasses to apply pieces
of knowledge by practice

Any class object in python 3. X is an instance of type class

If we want to create our own metaclass we need to inheritance
the type class and to implement class protocol
"""


class UselessMeta(type):

    def __new__(mcs, *args, **kwargs):
        print('I am useless metaclass. I just print arguments in __new__')
        print(mcs, args, kwargs)
        return type.__new__(mcs, *args, **kwargs)


class Doge(metaclass=UselessMeta):

    def __init__(self, doge_name: str) -> None:
        self.doge_name = doge_name

    def voice(self):
        print(f'Doge <{self.doge_name}> says: Aw aw aw!')


if __name__ == '__main__':
    good_boy = Doge('good_boy')
