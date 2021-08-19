from .traincar import Traincar
from typing import List


class Train:
    def __init__(self):
        self.__train_cars: List[Traincar] = []

    def add_traincar(self, traincar: Traincar):
        self.__train_cars.append(traincar)

    # well it should not be property -1 point
    # Here is error: TypeError: 'list' object is not callable -1 point
    @property
    def __str__(self):
        train_list = []
        for item in self.__train_cars:
            string = f'Train car #{item.get_car_number}'
            train_list.append(string)
        return train_list
