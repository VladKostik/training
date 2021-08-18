from HW_str import Harley


if __name__ == '__main__':
    dyna = Harley(
            'Dyna FXDC',
            2012,
            'gasoline',
            'manual 6 speed',
            'belt',
            'TwinCam 96',
            2,
            1580,
            70,
            4.8,
            'telescopic fork 49 mm',
            'swing-arm with 2 shock absorbers',
            '280 mm disc with 2 break calipers',
            '230 mm disc with one break caliper'
        )
    print(dyna.__str__)
    