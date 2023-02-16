from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

def test_entry_button_sign_in(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text  # поиск по атрибуту
    assert check == 'Соберите бургер'

def test_entry_personal_account_button(driver):
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text  # поиск по атрибуту
    assert check == 'Соберите бургер'

def test_entry_button_in_registration_form(driver):
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.register_link)))
    driver.find_element(By.XPATH, config.register_link).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.come_in)))
    driver.find_element(By.XPATH, config.come_in).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text  # поиск по атрибуту
    assert check == 'Соберите бургер'

def test_entry_button_in_password_recovery_form(driver):
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.forgot_password)))
    driver.find_element(By.XPATH, config.forgot_password).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.come_in)))
    driver.find_element(By.XPATH, config.come_in).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"))).text  # поиск по атрибуту
    assert check == 'Соберите бургер'