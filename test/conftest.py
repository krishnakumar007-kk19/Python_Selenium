from selenium import webdriver
import pytest


@pytest.fixture
def browser_instance():
    driver=webdriver.Chrome()
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    yield driver
    driver.quit()


