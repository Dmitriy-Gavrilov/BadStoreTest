import pytest
from selenium.webdriver.common.by import By
from autotests.utils import wait_of_element_located


def add_to_cart(driver, count_items, first_item=2):
    for i in range(first_item, first_item + count_items):
        checkbox = driver.find_element(By.XPATH,
                                       f"/html/body/table[2]/tbody/tr/td[3]/font/form/table/tbody/tr[{i}]/td[6]/input")
        checkbox.click()

    submit_btn = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[1]")
    submit_btn.click()


@pytest.mark.parametrize("count_items, expected_count", [
    (0, 0),
    (2, 2),
    (8, 8)
])
def test_add_items(driver, count_items, expected_count):
    add_to_cart(driver, count_items)

    to_cart_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    to_cart_btn.click()
    if expected_count:
        result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h3")
        items_count = int(result_str.text.split()[2])
        assert items_count == expected_count
    else:
        result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
        assert result_str.text == "You have no items in your cart."


def test_add_to_existing(driver):
    add_to_cart(driver, 3)

    catalog_link = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[1]/a")
    catalog_link.click()

    add_to_cart(driver, 1, 5)

    to_cart_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    to_cart_btn.click()
    result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h3")
    items_count = int(result_str.text.split()[2])

    assert items_count == 4
