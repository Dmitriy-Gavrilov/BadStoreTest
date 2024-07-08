import pytest
from selenium.webdriver.common.by import By
from autotests.utils import find_greet_text


def auth(driver, email, password):
    # Поиск элементов на странице
    login_element = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/input")
    password_element = driver.find_element(by=By.XPATH,
                                           value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[1]/input")
    auth_button = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[2]/input")

    # Заполнение полей и нажатие на кнопку
    login_element.send_keys(email)
    password_element.send_keys(password)
    auth_button.click()


@pytest.mark.parametrize("email,password, expected_result", [
    ("abcd@gmail.com", "abcd", "Dmitriy"),
    ("", "", "{Unregistered User}"),
    ("--123", "...", "{Unregistered User}"),
    ("123@123.com", "password", "{Unregistered User}"),
])
def test_auth(driver, email, password, expected_result):
    auth(driver, email, password)
    assert find_greet_text(driver).text == expected_result
