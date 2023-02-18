from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import time


def test_go_to_sauces(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.sauces)))
    driver.find_element(By.XPATH, config.sauces).click()
    check = driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute("class") # поиск по узлу-родителю
    assert 'tab_tab_type_current__2BEPc' in check

def test_go_to_stuffing(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.stuffing)))
    driver.find_element(By.XPATH, config.stuffing).click()
    check = driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute("class") # поиск по узлу-родителю
    assert 'tab_tab_type_current__2BEPc' in check

def test_go_to_buns(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.buns)))
    driver.find_element(By.XPATH, config.stuffing).click()
    time.sleep(3)
    driver.find_element(By.XPATH, config.buns).click()
    time.sleep(3)
    check = driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute("class") # поиск по узлу-родителю
    assert 'tab_tab_type_current__2BEPc' in check