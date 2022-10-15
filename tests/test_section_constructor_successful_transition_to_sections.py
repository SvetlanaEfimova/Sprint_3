from selenium.webdriver.common.by import By
from locators import bread_section, sauces_section, bread, sauce, fillings_section, filling


def test_go_to_the_bread_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, sauces_section).click()
    driver.find_element(By.XPATH, bread_section).click()
    assert bread is not None


def test_go_to_the_sauces_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, sauces_section).click()
    assert sauce is not None


def test_go_to_the_fillings_section_successfully(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.XPATH, fillings_section).click()
    assert filling is not None
