import pytest
from autotests.pages.account_page import AccountPage
from autotests.pages.login_page import LoginPage
from autotests.utils import find_greet_text


@pytest.mark.parametrize("email,password,new_name,new_email,expected_result", [
    ("abcd@gmail.com", "abcd", "New Name", "newemail@gmail.com", "New Name"),
    ("abcd@gmail.com", "abcd", "", "", "New Name"),
])
def test_change_account_info(driver, email, password, new_name, new_email, expected_result):
    login_page = LoginPage(driver)
    login_page.login(email, password)
    account_page = AccountPage(driver)
    account_page.change_account_info(new_name, new_email)
    assert find_greet_text(driver).text == expected_result
