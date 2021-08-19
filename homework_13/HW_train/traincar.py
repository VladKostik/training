from .passenger import Passenger


class Traincar:
    def __init__(self, car_number: int):
        self.__car_number = car_number
        self.__passengers_list = []

    def add_passenger(self, passenger: Passenger):
        if len(self.__passengers_list) > 9:
            raise Exception(f'There are no free seat in this train car!')
        self.__passengers_list.append(passenger)

    # I suggest to name it like number since we alrady know that it is train car -1 point
    @property
    def get_car_number(self):
        return self.__car_number

    # it should not be property since you will get this error -1 point
    # TypeError: 'str' object is not callable
    @property
    def __str__(self):
        """Returns train car number"""
        return f'[{self.get_car_number}]'

    # it should not be a property since you will get this error: -1 point
    # TypeError: 'int' object is not callable
    @property
    def __len__(self):
        """Returns number of passengers in the train car"""
        return len(self.__passengers_list)
