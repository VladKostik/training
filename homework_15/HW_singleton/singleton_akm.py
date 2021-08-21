from typing import Type


def singleton_akm(_class: Type):

    def inner(*args):
        if not hasattr(_class, '__instance'):
            setattr(_class, '__instance', _class(*args))
        return getattr(_class, '__instance')
    return inner


# nice but instance not private attribute. I can get it from global scope withou
# any additional manipulations -3 points
