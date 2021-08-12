from homework_14.HW_14.dir_hw14.create_human import create_human


if __name__ == '__main__':
    for human in create_human({'John': 33, 'Marta': 28, 'Jack': 36}):
        print(human.get_info())
        print(human.get_action())
