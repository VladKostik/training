class Company:

    def __init__(
            self,
            name: str,
            comp_type: str,
            location: str,
            seed_capital: int
    ):
        self.name = name
        self.comp_type = comp_type
        self.location = location
        self.seed_capital = seed_capital

    def get_info(self) -> str:
        """
        Returns general information about company
        """
        return f'{self.name} {self.comp_type} located in {self.location}\n' \
               f'Seed capital of {self.name} {self.comp_type} is USD{self.seed_capital}'

    @staticmethod
    def hire() -> None:
        """
        Describes the employees hiring process
        """
        pass

    def produce(self):
        """
        Describes goods producing
        """
        pass

    def make_money(self) -> None:
        """
        Shows how the company makes money
        """
        pass


if __name__ == '__main__':
    toshiba: Company = Company('Toshiba', 'Corp.', 'Japan', 4000000)
    print(toshiba.get_info())

    # Good but I want to see in methods state modification. -2 points
    # All fields are public so I can modify them from anywhere in global scope -2 points

    # toshiba.name = "Ololo"
    # TODO: hide all fields using__
    # TODO: add method hire for example which will increase number of employees and add employee into the list of names for example

