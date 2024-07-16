import pytest
from autotests.pages.cart_page import CartPage
from autotests.utils import wait_of_element_located


@pytest.mark.parametrize("count_items,expected_count", [
    (0, 0),
    (2, 2),
    (8, 8)
])
def test_add_items(driver, count_items, expected_count):
    cart_page = CartPage(driver)
    cart_page.add_to_cart(count_items)
    cart_page.go_to_cart()
    if expected_count:
        result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h3")
        items_count = int(result_str.text.split()[2])
        assert items_count == expected_count
    else:
        result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
        assert result_str.text == "You have no items in your cart."


def test_add_to_existing(driver):
    cart_page = CartPage(driver)
    cart_page.add_to_cart(3)
    catalog_link = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[1]/a")
    catalog_link.click()
    cart_page.add_to_cart(1, 5)
    cart_page.go_to_cart()
    result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h3")
    items_count = int(result_str.text.split()[2])
    assert items_count == 4
