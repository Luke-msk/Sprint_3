from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random

faker = Faker()

def test_registration_success(driver):
    name = faker.name()
    email = faker.email()
    password = random.randint(111111,999999)
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click() # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(name) # поиск по относительному пути
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email) # поиск по относительному пути
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(password) # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # поиск по узлу-тексту внутри тега
    reg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//main/div"))).get_attribute("class") # поиск по относительному пути
    assert reg == 'Auth_login__3hAey'

def test_registration_fail(driver):
    name = faker.name()
    email = faker.email()
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(name)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('123')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # поиск по узлу-тексту внутри тега
    assert driver.find_element(By.XPATH,".//fieldset[3]/div/p[text()]").text == 'Некорректный пароль'  # поиск по узлу-тексту внутри тега