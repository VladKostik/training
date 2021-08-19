from .passenger import Passenger


class Traincar:
    def __init__(self, car_number: int):
        self.__car_number = car_number
        self.__passengers_list = []

    def add_passenger(self, passenger: Passenger):
        if len(self.__passengers_list) > 9:
            raise Exception(f'There are no free seat in this train car!')
        self.__passengers_list.append(passenger)

    @property
    def get_car_number(self):
        return self.__car_number

    @property
    def __str__(self):
        """Returns train car number"""
        return f'[{self.get_car_number}]'

    @property
    def __len__(self):
        """Returns number of passengers in the train car"""
        return len(self.__passengers_list)
