from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_entry_button_sign_in(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com') # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517) # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # поиск по узлу-тексту внутри тега
    entry = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//section[2]/div/button[text()]"))).text # поиск по относительному пути
    assert entry == 'Оформить заказ'

def test_entry_personal_account_button(driver):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    entry = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//section[2]/div/button[text()]"))).text # поиск по относительному пути
    assert entry == 'Оформить заказ'

def test_entry_button_in_registration_form(driver):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
    driver.find_element(By.XPATH, ".//a[@href='/login']").click() # поиск по атрибуту
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    entry = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//section[2]/div/button[text()]"))).text # поиск по относительному пути
    assert entry == 'Оформить заказ'

def test_entry_button_in_password_recovery_form(driver):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[@href='/forgot-password']")))
    driver.find_element(By.XPATH, ".//a[@href='/forgot-password']").click()  # поиск по атрибуту
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
    driver.find_element(By.XPATH, ".//a[@href='/login']").click()  # поиск по атрибуту
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    entry = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//section[2]/div/button[text()]"))).text # поиск по относительному пути
    assert entry == 'Оформить заказ'