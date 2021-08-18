from traincar import Traincar
from typing import List


class Train:
    def __init__(self):
        self.__train_cars: List[Traincar] = []

    def add_traincar(self, traincar: Traincar):
        self.__train_cars.append(traincar)

    @property
    def __str__(self):
        train_list = []
        for item in self.__train_cars:
            string = f'Train car #{item.car_number}'
            train_list.append(string)
        return train_list


if __name__ == '__main__':
    train1 = Train()
    traincar1 = Traincar(3)
    traincar2 = Traincar(4)
    train1.add_traincar(traincar1)
    train1.add_traincar(traincar2)
    print(train1.__str__)
    print(traincar1)
