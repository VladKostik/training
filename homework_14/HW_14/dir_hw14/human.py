from homework_14.HW_14.dir_hw14.action import Action


class Human:
    def __init__(self, name: str, age: int, action_name: str):
        self.name = name
        self.age = age
        self.__action = Action(action_name)

    def get_info(self):
        return f'Name: {self.name}\nAge: {self.age}'

    def get_action(self):
        return f'{self.name} is {Action.action(self.__action)}'

# no property action in class so -3 points
# property actio should return action field
