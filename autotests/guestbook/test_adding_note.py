import pytest
from selenium.webdriver.common.by import By


def find_fields(driver):
    name_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/table/tbody/tr[1]/td[2]/input")
    email_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/table/tbody/tr[2]/td[2]/input")
    text_input = driver.find_element(By.XPATH,
                                     "/html/body/table[2]/tbody/tr/td[3]/font/table/tbody/tr[3]/td[2]/textarea")

    return name_input, email_input, text_input


def fill_fields(driver, data):
    for ind, elem in enumerate(find_fields(driver)):
        elem.send_keys(data[ind])


@pytest.mark.parametrize("name, email, content, url", [
    ("Dmitriy", "abcd@gmail.com", "comment", "http://192.168.31.203/cgi-bin/badstore.cgi?action=doguestbook"),
    ("", "", "", "http://192.168.31.203/cgi-bin/badstore.cgi?action=guestbook"),
    ("Abc", "-?/", "content", "http://192.168.31.203/cgi-bin/badstore.cgi?action=guestbook"),
])
def test_add_note(driver, name, email, content, url):
    fill_fields(driver, [name, email, content])

    add_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/center/input[1]")
    add_btn.click()

    assert driver.current_url == url


def test_clear_fields(driver):
    fill_fields(driver, ["Abc", "abcd@gmail.com", "content"])

    clear_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/center/input[2]")
    clear_btn.click()

    assert all(i.text == "" for i in find_fields(driver))
