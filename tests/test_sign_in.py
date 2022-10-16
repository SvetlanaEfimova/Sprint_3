import ec as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import login_button, email_registration, password_registration, sign_in_button, main_page_title, \
    personal_account_button, button_in_the_registration_form, button_in_the_registration


def test_sign_in_home_page_button_successful_login(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_sign_in_personal_account_button_successful_login(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_sign_in_button_in_the_registration_form_successful_login(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, button_in_the_registration_form).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_sign_in_from_the_password_recovery_form(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, button_in_the_registration).click()
    driver.find_element(By.XPATH, button_in_the_registration_form).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, main_page_title)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

