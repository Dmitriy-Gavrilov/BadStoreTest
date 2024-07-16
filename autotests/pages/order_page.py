from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_order_form(self, address, city, state, zip_code, card_type, card_number, card_name):
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[1]").send_keys(address)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[2]").send_keys(city)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[3]").send_keys(state)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[4]").send_keys(zip_code)
        self.driver.find_element(By.XPATH,
                                 f"/html/body/table[2]/tbody/tr/td[3]/form/input[5][@value='{card_type}']").click()
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[6]").send_keys(card_number)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[7]").send_keys(card_name)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/input[8]").click()
