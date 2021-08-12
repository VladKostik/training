from homework_14.HW_14.dir_hw14.human import Human


def create_human(list_of: dict) -> list:
    humans = []
    for name, age in list_of.items():
        name = Human(f'{name}'.capitalize(), age)
        humans.append(name)
    return humans
