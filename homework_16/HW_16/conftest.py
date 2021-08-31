import pytest
from homework_16.HW_16.human import Human


@pytest.fixture
def human_1() -> Human:
    yield Human('Jah', 33, 'male')
