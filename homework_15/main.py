from HW_singleton import AKM
from HW_factory.product_factory import ProductFactory

if __name__ == '__main__':
    akm1 = AKM(7.62, 'wood')
    akm2 = AKM(5.45, 'steel')
    print(akm1.__instance)
    print(akm2)

    print(ProductFactory.get_product('apple'))
    print(ProductFactory.get_product('watermelon'))
    print(ProductFactory.get_product('plum'))

# I suppose there are no plum in store so I have error -1 point
#    raise Exception(f'Product name is incorrect! There is no '
# Exception: Product name is incorrect! There is no plum product in our store.