from .singleton_akm import singleton_akm


@singleton_akm
class AKM:
    def __init__(self, caliber: float, stock_type: str):
        self.__caliber = caliber
        self.__stock_type = stock_type
