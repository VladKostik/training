import pytest
from homework_16.HW_16.human import Human


def test_grow_method(human_1):
    human_1.grow()
    assert human_1.age == 34


def test_change_gender_method(human_1, monkeypatch):
    monkeypatch.setattr(human_1, '_Human__gender', 'male')
    human_1.change_gender('female')
    assert human_1.gender == 'female'


def test_change_gender_exception(human_1):
    with pytest.raises(Exception):
        human_1.change_gender('male')
    assert Exception


def test_gender_method(human_1):
    assert human_1.gender == 'male'


def test_age_method(human_1):
    assert human_1.age == 33


def test_gender_validation_method():
    human2 = Human('Anton', 26, 'fucking fagot')
    with pytest.raises(Exception):
        human2._Human__validate_gender(human2.gender)
    assert Exception


def test_is_alive_method_for_dead(human_1):
    with pytest.raises(Exception):
        for i in range(100):
            human_1.grow()
    assert human_1._Human__status == 'dead'


def test_is_alive_method_for_alive(human_1):
    for i in range(67):
        human_1.grow()
    assert human_1._Human__status == 'alive'
