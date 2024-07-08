from test_adding import *
from autotests.utils import find_cart_text


def test_delete_items(driver):
    add_to_cart(driver, 2)

    to_cart_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    to_cart_btn.click()

    cart_text_before = find_cart_text(driver)

    reset_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[2]")
    reset_btn.click()

    cart_text_after = find_cart_text(driver)

    assert cart_text_before != cart_text_after
