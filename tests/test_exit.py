from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

def test_exit_from_personal_account(driver):
    driver.find_element(By.XPATH, config.login_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.form_email)))
    driver.find_element(By.XPATH, config.form_email).send_keys(config.email)
    driver.find_element(By.XPATH, config.form_password).send_keys(config.password)
    driver.find_element(By.XPATH, config.entry_button).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.personal_area)))
    driver.find_element(By.XPATH, config.personal_area).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, config.exit_button)))
    driver.find_element(By.XPATH, config.exit_button).click()
    check = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"))).text
    assert check == 'Вход'