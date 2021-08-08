from homework_11.HW_11.motorcycle import Motorcycle


class HD(Motorcycle):
    name = 'Harley Davidson'

    def __init__(
            self,
            model: str,
            year_of_build: int,
            fuel: str,
            gear_type: str,
            main_gear: str,
            engine: str,
            number_of_cylinders: int,
            engine_capacity: float,
            power: int,
            fuel_capacity: float,
            front_suspension: str,
            rear_suspension: str,
            front_break: str,
            rear_break: str
    ):
        self.__model = model
        self.__year_of_build = year_of_build
        self.__fuel = fuel
        self.__gear_type = gear_type
        self.__main_gear = main_gear
        self.__engine = engine
        self.__number_of_cylinders = number_of_cylinders
        self.__engine_capacity = engine_capacity
        self.__power = power
        self.__fuel_capacity = fuel_capacity
        self.__front_suspension = front_suspension
        self.__rear_suspension = rear_suspension
        self.__front_break = front_break
        self.__rear_break = rear_break

    @property
    def get_specs(self) -> str:
        """
        Returns motorcycle specifications
        """
        return f'{self.name} {self.__model} specifications:\n' \
               f'\t--engine - {self.__engine}\n' \
               f'\t--fuel - {self.__fuel}\n' \
               f'\t--number of cylinders - {self.__number_of_cylinders}\n' \
               f'\t--engine capacity - {self.__engine_capacity}\n' \
               f'\t--power - {self.__power}\n' \
               f'\t--gear type - {self.__gear_type}\n' \
               f'\t--main gear - {self.__main_gear}\n' \
               f'\t--fuel capacity - {self.__fuel_capacity}\n' \
               f'\t--front suspension - {self.__front_suspension}\n' \
               f'\t--rear suspension - {self.__rear_suspension}\n' \
               f'\t--front break - {self.__front_break}\n' \
               f'\t--rear break - {self.__rear_break}'

    def move(self) -> str:
        """
        Describes moving of motorcycle
        """
        return f'{self.__model} moves as fuck'

    def refill(self) -> str:
        """
        Describes refilling of motorcycle`s tank with fuel
        """
        volume = 0.5
        while volume < self.__fuel_capacity-0.1:
            volume += 0.1
        return f'Filled {self.__model}`s tank with {volume.__round__(1)} ' \
               f'gallons of {self.__fuel}'
