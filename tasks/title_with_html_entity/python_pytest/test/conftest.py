import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox()
    driver.get("http://www.wordpress.org")
    request.cls.driver = driver

    yield driver
    driver.close()
