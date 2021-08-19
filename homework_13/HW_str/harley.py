class Harley:

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

    def __strip_key(self, key: str):
        return key.replace(f'_{self.__class__.__name__}__', '')

    # This also will not work if you will try print object without calling __str__ magc method manually
    @property
    def __str__(self) -> str:
        """
        Returns motorcycle specifications
        """
        string = f'{__class__.__name__}: ' + '{\n'
        for key, value in self.__dict__.items():
            string += f'\t{self.__strip_key(key)}: {value}\n'
        return string + '}'
