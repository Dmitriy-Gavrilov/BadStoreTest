from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.full_name_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form[2]/input")
        self.email_input = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[1]/input")
        self.password_input = driver.find_element(By.XPATH,
                                                  "/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[2]/input")
        self.register_button = driver.find_element(By.XPATH,
                                                   "/html/body/table[2]/tbody/tr/td[3]/font/form[2]/p[5]/input[2]")

    def register(self, full_name: str, email: str, password: str):
        self.full_name_input.send_keys(full_name)
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.register_button.click()
