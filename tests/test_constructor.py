from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

def test_go_to_constructor(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.personal_area)))
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.constructor)))
    driver.find_element(By.XPATH, config.constructor).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text # поиск по атрибуту
    assert check == 'Соберите бургер'

def test_go_to_logo(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.personal_area)))
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.logo)))
    driver.find_element(By.XPATH, config.logo).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text # поиск по относительному пути
    assert check == 'Соберите бургер'