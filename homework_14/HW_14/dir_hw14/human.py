from homework_14.HW_14.dir_hw14.action import Action


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class_action = Action.action_name

    def get_info(self):
        return f'Name: {self.name}\nAge: {self.age}'

    def get_action(self):
        return f'{self.name} is {self.__class_action}'
