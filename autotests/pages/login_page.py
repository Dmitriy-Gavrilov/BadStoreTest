from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form[1]/input")
        self.password_input = driver.find_element(By.XPATH,
                                                  "/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[1]/input")
        self.auth_button = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form[1]/p[2]/input")

    def login(self, email: str, password: str):
        self.login_input.send_keys(email)
        self.password_input.send_keys(password)
        self.auth_button.click()
