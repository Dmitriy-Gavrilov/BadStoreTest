import pytest
from selenium.webdriver.common.by import By
from autotests.utils import find_greet_text


def register(driver, full_name, email, password):
    full_name_element = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[2]/input")
    email_element = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[1]/input")
    password_element = driver.find_element(by=By.XPATH,
                                           value="/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[2]/input")
    register_button = driver.find_element(by=By.XPATH,
                                          value="/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[5]/input[2]")

    full_name_element.send_keys(full_name)
    email_element.send_keys(email)
    password_element.send_keys(password)
    register_button.click()


@pytest.mark.parametrize("full_name,email,password, expected_result", [
    ("User", "abcd@gmail.com", "abcd", "User"),
    ("", "", "", "{Unregistered User}"),
    ("User", "abcd.ru", "password", "{Unregistered User}"),
    ("User", "&)^", "password", "{Unregistered User}"),
    ("User", "abcd@gmail.com", "-)/", "{Unregistered User}"),
])
def test_registration(driver, full_name, email, password, expected_result):
    register(driver, full_name, email, password)
    assert find_greet_text(driver).text == expected_result
