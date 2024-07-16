from autotests.pages.cart_page import CartPage
from autotests.utils import wait_of_element_located


def test_clear_cart(driver):
    cart_page = CartPage(driver)
    cart_page.add_to_cart(3)
    cart_page.go_to_cart()
    cart_page.clear_cart()
    result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
    assert result_str.text == "You have no items in your cart."
