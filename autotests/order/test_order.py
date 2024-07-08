import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from autotests.login.test_registration import register
from autotests.cart.test_adding import add_to_cart


def order(driver, card_number, date, email=None):
    card_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[1]/input[1]")
    date_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/p[1]/input[2]")

    card_input.send_keys(card_number)
    date_input.send_keys(date)

    if email:
        email_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/input")
        email_input.send_keys(email)

    order_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/p[2]/input")
    order_btn.click()


@pytest.mark.parametrize("email, card_number, date, alert_text", [
    ("abcd@gmail.com", "5536914058056216", "22/29", "Thank you for using MasterCard!"),
    ("", "", "", "You haven't entered enough information!"),
    ("-&/", "5536914058056216", "22/29", "Only valid numbers are allowed - and no spaces or dashes!"),
    ("abcd@gmail.com", "6437829-j,", "22/29", "Only valid numbers are allowed - and no spaces or dashes!"),
    ("abcd@gmail.com", "5536914058056216", "-=.?", "Only valid numbers are allowed - and no spaces or dashes!"),
])
def test_payment(driver, email, card_number, date, alert_text):
    order(driver, card_number, date, email)

    alert = WebDriverWait(driver, 1).until(EC.alert_is_present())

    assert alert.text == alert_text


def test_previous_orders(driver):
    order_url = driver.current_url

    driver.get("http://192.168.31.203/cgi-bin/badstore.cgi?action=whatsnew")
    add_to_cart(driver, 2)

    driver.get(order_url)

    order(driver, "5536914058056216", "22/29", "abcd@gmail.com")

    alert = WebDriverWait(driver, 1).until(EC.alert_is_present())
    alert.accept()

    previous_orders_link = driver.find_element(By.XPATH,
                                               "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[3]/a")
    previous_orders_link.click()

    items = driver.find_elements(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/p[1]/table")

    assert items


def test_previous_orders_auth(driver):
    order_url = driver.current_url

    driver.get("http://192.168.31.203/cgi-bin/badstore.cgi?action=loginregister")
    register(driver, "User", "qwerty@gmail.com", "password123")

    driver.get("http://192.168.31.203/cgi-bin/badstore.cgi?action=whatsnew")
    add_to_cart(driver, 2)

    driver.get(order_url)
    order(driver, "5536914058056216", "22/29")

    alert = WebDriverWait(driver, 1).until(EC.alert_is_present())
    alert.accept()

    previous_orders_link = driver.find_element(By.XPATH,
                                               "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[3]/a")
    previous_orders_link.click()

    items = driver.find_elements(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/p[1]/table")

    assert items
