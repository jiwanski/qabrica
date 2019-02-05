# how to run

Open terminal in **title_with_html_entity/python_pytest** directory and execute:

`python -m pytest -v`

## sample output

```shell
============================= test session starts ==============================
platform linux2 -- Python 2.7.12, pytest-3.9.2, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: ~/projects/github/qabrica/tasks/title_with_html_entity/python_pytest, inifile:
collected 1 item                                                               

test/test_title_with_html_entity.py::Test::test_verify_title PASSED      [100%]

========================== 1 passed in 12.45 seconds ===========================
qabrica@localhost~/projects/github/qabrica/tasks/title_with_html_entity/python_pytest> 
```

> Using pytest framework with fixtures to provide test *setup* and *teardown*.

> Concept taken from https://www.seleniumeasy.com/python/webdriver-tests-in-pytest-using-fixtures-and-conftest
