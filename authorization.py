import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_of_element_located(driver, xpath):
    return WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)))


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://192.168.31.203/cgi-bin/badstore.cgi?action=loginregister")
    yield driver
    driver.quit()


def test_auth(driver):
    # Поиск элементов на странице
    login = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/input")
    password = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[1]/input")
    auth_button = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[2]/input")

    # Заполнение полей и нажатие на кнопку
    login.send_keys("abcd@gmail.com")
    password.send_keys("abcd")
    auth_button.click()

    # Переключение на страницу с приветствием
    iframe = driver.find_element(by=By.XPATH,
                                 value="/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[1]/iframe")
    driver.switch_to.frame(iframe)

    # Проверка надписи приветствия
    greet_text = wait_of_element_located(driver, "/html/body/font/b")
    assert greet_text.text != "{Unregistered User}"

    driver.switch_to.default_content()
