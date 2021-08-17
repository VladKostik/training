from .iproduct import IProduct
from .apple import Apple
from .pear import Pear
from .potato import Potato
from .watermelon import Watermelon


class ProductFactory:

    @staticmethod
    def get_product(product_name: str) -> IProduct:
        if product_name == 'apple':
            return Apple()
        elif product_name == 'pear':
            return Pear()
        elif product_name == 'potato':
            return Potato()
        elif product_name == 'watermelon':
            return Watermelon()
        else:
            raise Exception(f'Product name is incorrect! There is no '
                            f'{product_name} product in our store.')
