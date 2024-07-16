import pytest
from autotests.pages.login_page import LoginPage
from autotests.utils import find_greet_text


@pytest.mark.parametrize("email,password,expected_result", [
    ("abcd@gmail.com", "abcd", "Dmitriy"),
    ("", "", "{Unregistered User}"),
    ("--123", "...", "{Unregistered User}"),
    ("123@123.com", "password", "{Unregistered User}"),
])
def test_auth(driver, email, password, expected_result):
    login_page = LoginPage(driver)
    login_page.login(email, password)
    assert find_greet_text(driver).text == expected_result
