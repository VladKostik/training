class Traincar:
    def __init__(self, car_number: int):
        self.__car_number = car_number
        self.__passengers = list()

    # def __str__(self):
    #     result = "[\n"
    #
    #     for passenger in self.__passengers:
    #         result += f"\t{passenger}"
    #
    #     return result + "\n]"
    #
    # def add_passenger(self, passenger: Passenger):
    #     self.__passengers.append(passenger)

    @property
    def car_number(self):
        return self.__car_number
