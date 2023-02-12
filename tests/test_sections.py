from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_sauces(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//span[text()='Соусы']")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click() # поиск по узлу-тексту внутри тега
    check = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]").get_attribute("class") # поиск по относительному пути
    assert 'tab_tab_type_current__2BEPc' in check

def test_go_to_stuffing(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//span[text()='Начинки']")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()  # поиск по узлу-тексту внутри тега
    check = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]").get_attribute("class") # поиск по относительному пути
    assert 'tab_tab_type_current__2BEPc' in check

def test_go_to_buns(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//span[text()='Начинки']")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()  # поиск по узлу-тексту внутри тега
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()  # поиск по узлу-тексту внутри тега
    check = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").get_attribute("class")  # поиск по относительному пути
    assert 'tab_tab_type_current__2BEPc' in check