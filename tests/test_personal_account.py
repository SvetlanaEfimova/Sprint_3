from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import login_button, email_registration, password_registration, sign_in_button, \
    personal_account_button, button_profile, button_constructor, logo, button_log_out, button_for_placing_an_order


def test_click_through_to_your_personal_account(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_switching_from_your_personal_account_to_the_constructor(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, button_constructor)))
    driver.find_element(By.XPATH, button_constructor).click()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_switching_from_your_personal_account_to_the_logo(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, logo).click()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, button_for_placing_an_order)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_log_out_of_your_account_successful_log_out(driver, user_created):
    email, password = user_created()
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, email_registration).send_keys(email)
    driver.find_element(By.XPATH, password_registration).send_keys(password)
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, personal_account_button)))
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, button_profile)))
    driver.find_element(By.XPATH, button_log_out).click()
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, sign_in_button)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()