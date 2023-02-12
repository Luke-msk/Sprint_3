from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_exit_from_personal_account(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys('arogers@example.com')  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(492517)  # поиск по относительному пути
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//p[text()='Личный Кабинет']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  # поиск по узлу-тексту внутри тега
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//li[3]/button[text()='Выход']")))
    driver.find_element(By.XPATH, ".//li[3]/button[text()='Выход']").click()  # поиск по узлу-тексту внутри тега
    exit = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//main/div/h2[text()]"))).text # поиск по относительному пути
    assert exit == 'Вход'