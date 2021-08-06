from HW_11.hd import HD


if __name__ == '__main__':
    dyna = HD(
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

    print(dyna.get_specs)
    print(dyna.move())
    print(dyna.turn_right())
    print(dyna.refill())
    print(dyna.turn_left())
    print(dyna.stop())
