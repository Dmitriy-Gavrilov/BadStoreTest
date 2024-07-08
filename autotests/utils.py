from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_of_element_located(driver, xpath):
    return WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)))


def find_greet_text(driver):
    iframe = driver.find_element(by=By.XPATH,
                                 value="/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[1]/iframe")
    driver.switch_to.frame(iframe)

    return wait_of_element_located(driver, "/html/body/font/b")


def find_cart_text(driver):
    iframe = driver.find_element(by=By.XPATH,
                                 value="/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[1]/iframe")
    driver.switch_to.frame(iframe)

    cart_text = wait_of_element_located(driver, "/html/body/font")

    driver.switch_to.default_content()

    return cart_text
