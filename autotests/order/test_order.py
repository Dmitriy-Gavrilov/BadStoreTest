import pytest
from autotests.pages.cart_page import CartPage
from autotests.pages.order_page import OrderPage
from autotests.utils import wait_of_element_located


@pytest.mark.parametrize("count_items,address,city,state,zip_code,card_type,card_number,card_name,expected_text", [
    (3, "address", "city", "state", "zip_code", "Visa", "1234567890123456", "John Doe", "Thank you for your order!"),
    (0, "address", "city", "state", "zip_code", "Visa", "1234567890123456", "John Doe",
     "You have no items in your cart."),
])
def test_order(driver, count_items, address, city, state, zip_code, card_type, card_number, card_name, expected_text):
    cart_page = CartPage(driver)
    cart_page.add_to_cart(count_items)
    cart_page.go_to_cart()
    if count_items > 0:
        order_button = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[1]")
        order_button.click()
        order_page = OrderPage(driver)
        order_page.fill_order_form(address, city, state, zip_code, card_type, card_number, card_name)
    result_str = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
    assert result_str.text == expected_text
