# how to run

Open terminal in **harshad_numbers** directory and execute:

`python -m pytest -v`

## sample output

```shell
qabrica@localhost~/projects/github/qabrica/tasks/harshad_numbers> python -m pytest -v
========================================================================== test session starts ===========================================================================
platform linux2 -- Python 2.7.12, pytest-3.9.2, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: ~/projects/github/qabrica/tasks/harshad_numbers, inifile:
collected 10 items                                                                                                                                                       

python_pytest/test/test_harshad_numbers.py::test_is_valid[20-True] PASSED                                                                                          [ 10%]
python_pytest/test/test_harshad_numbers.py::test_is_valid[21-True] PASSED                                                                                          [ 20%]
python_pytest/test/test_harshad_numbers.py::test_is_valid[22-False] PASSED                                                                                         [ 30%]
python_pytest/test/test_harshad_numbers.py::test_get_next[0-1] PASSED                                                                                              [ 40%]
python_pytest/test/test_harshad_numbers.py::test_get_next[1-2] PASSED                                                                                              [ 50%]
python_pytest/test/test_harshad_numbers.py::test_get_next[17-18] PASSED                                                                                            [ 60%]
python_pytest/test/test_harshad_numbers.py::test_get_series[10-expected0] PASSED                                                                                   [ 70%]
python_pytest/test/test_harshad_numbers.py::test_get_series[20-expected1] PASSED                                                                                   [ 80%]
python_pytest/test/test_harshad_numbers.py::test_get_series_default[10-10-expected0] PASSED                                                                        [ 90%]
python_pytest/test/test_harshad_numbers.py::test_get_series_default[10-1000-expected1] PASSED                                                                      [100%]

======================================================================= 10 passed in 0.09 seconds ========================================================================
```