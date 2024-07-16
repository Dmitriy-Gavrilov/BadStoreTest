import pytest
from autotests.pages.registration_page import RegistrationPage
from autotests.utils import find_greet_text


@pytest.mark.parametrize("full_name,email,password,expected_result", [
    ("User", "abcd@gmail.com", "abcd", "User"),
    ("", "", "", "{Unregistered User}"),
    ("User", "abcd.ru", "password", "{Unregistered User}"),
    ("User", "&)^", "password", "{Unregistered User}"),
    ("User", "abcd@gmail.com", "-)/", "{Unregistered User}"),
])
def test_registration(driver, full_name, email, password, expected_result):
    registration_page = RegistrationPage(driver)
    registration_page.register(full_name, email, password)
    assert find_greet_text(driver).text == expected_result
