from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AccountPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def change_account_info(self, new_name: str, new_email: str):
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[1]").send_keys(new_name)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[2]").clear()
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[2]").send_keys(new_email)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[3]").click()
