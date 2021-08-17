from abc import ABC


class IProduct(ABC):
    _product_name: str = ''

    def __init__(self):
        self._units = 'kg'

    @property
    def get_units(self):
        return self._units
