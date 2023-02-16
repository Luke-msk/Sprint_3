from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import config

faker = Faker()

def test_registration_success(driver):
    name = faker.name()
    email = faker.email()
    password = random.randint(111111,999999)
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.register_link)))
    driver.find_element(By.XPATH, config.register_link).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_name)))
    driver.find_element(By.XPATH, config.form_name).send_keys(name)
    driver.find_element(By.XPATH, config.form_email).send_keys(email)
    driver.find_element(By.XPATH, config.form_password).send_keys(password)
    driver.find_element(By.XPATH, config.register_button).click()
    reg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//main/div"))).get_attribute("class") # поиск по относительному пути
    assert reg == 'Auth_login__3hAey'

def test_registration_fail(driver):
    name = faker.name()
    email = faker.email()
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.register_link)))
    driver.find_element(By.XPATH, config.register_link).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_name)))
    driver.find_element(By.XPATH, config.form_name).send_keys(name)
    driver.find_element(By.XPATH, config.form_email).send_keys(email)
    driver.find_element(By.XPATH, config.form_password).send_keys('123')
    driver.find_element(By.XPATH, config.register_button).click()
    assert driver.find_element(By.XPATH, ".//p[@class = 'input__error text_type_main-default']").text == 'Некорректный пароль'  # поиск по атрибуту