import pytest
from selenium.webdriver.common.by import By
from autotests.login.test_registration import register
from autotests.utils import wait_of_element_located


@pytest.mark.parametrize("new_name, new_email, new_password, verify_password, expected_name", [
    ("User2", "abcde@gmail.com", "pswd", "pswd", "User2"),
    ("", "", "", "", "User"),
    ("User2", "", "", "", "User2"),
    ("User2", "", "123", "1234", "User"),
])
def test_change_name_auth(driver, new_name, new_email, new_password, verify_password, expected_name):
    account_url = driver.current_url

    driver.get("http://192.168.31.203/cgi-bin/badstore.cgi?action=loginregister")
    register(driver, "User", "qwerty@gmail.com", "password123")

    driver.get(account_url)

    new_name_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[1]/input")
    new_email_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[3]/input")
    new_password_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[4]/input[1]")
    verify_password_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[4]/input[2]")

    new_name_input.send_keys(new_name)
    new_email_input.send_keys(new_email)
    new_password_input.send_keys(new_password)
    verify_password_input.send_keys(verify_password)

    change_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[5]/input[3]")
    change_btn.click()

    driver.get(account_url)
    updated_name = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")

    assert updated_name.text.split(", ")[1] == expected_name
