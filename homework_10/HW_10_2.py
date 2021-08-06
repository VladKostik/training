class Employee:

    def __init__(
            self,
            name: str,
            sure_name: str,
            age: int,
            employed_in: str,
            position: str,
            salary: int,
            actions: str
    ):
        self.__name = name
        self.__sure_name = sure_name
        self.__age = age
        self.__employed_in = employed_in
        self.__position = position
        self.__salary = salary
        self.__actions = actions

    def get_info_employee(self) -> str:
        """
        Returns info about employee
        """
        return f'{self.__name} {self.__sure_name}, {self.__age} years old, ' \
               f'employed in {self.__employed_in} as {self.__position}\nSalary: {self.__salary}'

    def change_salary(self, salary) -> None:
        """
        Changes employee`s salary
        """
        self.__salary = salary

    def do_the_job(self) -> str:
        """
        Describes employee`s duties
        """
        return f'{self.__name} {self.__sure_name} is {self.__actions}'

    @property
    def current_task(self) -> str:
        """
        Access to employee`s actions
        """
        return self.__actions

    @current_task.setter
    def current_task(self, new_task: str) -> None:
        """
        Sets a new task for employee
        """
        self.__actions = new_task


if __name__ == '__main__':
    employee_1: Employee = Employee(
        'John',
        'Rambo',
        33,
        'U.S. Marine Corps',
        'machine-gunner',
        3000,
        'killing commies for mummy'
    )
    employee_1.change_salary(5000)
    print(employee_1.get_info_employee())
    print(employee_1.do_the_job())
    print(employee_1.current_task)
    employee_1.current_task = 'searching for FIM-92 Stingers'
    print(employee_1.do_the_job())
