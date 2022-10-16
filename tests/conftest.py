import string
import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import name, email_registration, password_registration, register_button


def random_str(lenght):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(lenght))


@pytest.fixture
def driver():
    return webdriver.Chrome()


@pytest.fixture()
def user_created(driver):
    def create():
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, name).send_keys(random_str(5))
        email = f'{random_str(6)}@ya.ru'
        driver.find_element(By.XPATH, email_registration).send_keys(email)
        password = random_str(7)
        driver.find_element(By.XPATH, password_registration).send_keys(password)
        driver.find_element(By.XPATH, register_button).click()
        return email, password
    return create


