# from HW_str import Harley
from HW_train.train import Train
from HW_train.traincar import Traincar
from HW_train.passenger import Passenger


if __name__ == '__main__':
    # dyna = Harley(
    #         'Dyna FXDC',
    #         2012,
    #         'gasoline',
    #         'manual 6 speed',
    #         'belt',
    #         'TwinCam 96',
    #         2,
    #         1580,
    #         70,
    #         4.8,
    #         'telescopic fork 49 mm',
    #         'swing-arm with 2 shock absorbers',
    #         '280 mm disc with 2 break calipers',
    #         '230 mm disc with one break caliper'
    #     )
    # print(dyna.__str__)

    train1 = Train()

    traincar1 = Traincar(1)
    traincar2 = Traincar(3)
    traincar3 = Traincar(2)

    train1.add_traincar(traincar1)
    train1.add_traincar(traincar2)
    train1.add_traincar(traincar3)

    passenger1 = Passenger('Arthur', 5)
    passenger2 = Passenger('Jack', 2)
    passenger3 = Passenger('Muhammed', 6)

    traincar1.add_passenger(passenger1)
    traincar1.add_passenger(passenger3)
    traincar2.add_passenger(passenger2)
    traincar3.add_passenger(passenger3)

    print(train1.__str__)
    print(traincar1.__len__)
    print(traincar1.__str__)
