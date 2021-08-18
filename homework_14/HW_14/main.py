from homework_14.HW_14.dir_hw14.human import Human


if __name__ == '__main__':
    bob = Human('Bob', 33, 'smoking weed')
    marta = Human('Marta', 26, 'reading Holy Bible')
    jack = Human('Jack', 38, 'drinking beer')
    humans = [bob, marta, jack]

    for human in humans:
        print(human.get_action())
