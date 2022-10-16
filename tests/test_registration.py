from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import random_str
from locators import name, email_registration, password_registration, register_button, invalid_password_error
from selenium.webdriver.support import expected_conditions as ec


def test_sign_in_home_page_button_successful_login(driver, user_created):
    user_created()
    WebDriverWait(driver, 5).until(ec.url_matches('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_registration_incorrect_password_registration_error():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, name).send_keys(random_str(5))
    driver.find_element(By.XPATH, email_registration).send_keys(f'{random_str(6)}@ya.ru')
    driver.find_element(By.XPATH, password_registration).send_keys(random_str(4))
    driver.find_element(By.XPATH, register_button).click()
    assert invalid_password_error is not None

    driver.quit()
