import pytest
from src import harshad_numbers

params_is_valid = [(20, True),
                   (21, True),
                   (22, False)]

params_get_next = [(0, 1),
                   (1, 2),
                   (17, 18)]

params_get_series = [(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                     (20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42])]

params_get_series_default = [(10, 10, [12, 18, 20, 21, 24, 27, 30, 36, 40, 42]),
                             (10, 1000, [1002, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1020])]


@pytest.mark.parametrize("param, expected", params_is_valid)
def test_is_valid(param, expected):
    assert harshad_numbers.Harshad.is_valid(param) is expected


@pytest.mark.parametrize("param, expected", params_get_next)
def test_get_next(param, expected):
    assert harshad_numbers.Harshad.get_next(param) == expected


@pytest.mark.parametrize("param, expected", params_get_series)
def test_get_series(param, expected):
    assert harshad_numbers.Harshad.get_series(param) == expected


@pytest.mark.parametrize("param1, param2, expected", params_get_series_default)
def test_get_series_default(param1, param2, expected):
    assert harshad_numbers.Harshad.get_series(param1, param2) == expected
