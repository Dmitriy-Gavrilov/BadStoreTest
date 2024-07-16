from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_to_cart(self, count_items: int, first_item: int = 2):
        for i in range(first_item, first_item + count_items):
            checkbox = self.driver.find_element(By.XPATH,
                                                f"/html/body/table[2]/tbody/tr/td[3]/font/form/table/tbody/tr[{i}]/td[6]/input")
            checkbox.click()
        submit_btn = self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[1]")
        submit_btn.click()

    def go_to_cart(self):
        to_cart_btn = self.driver.find_element(By.XPATH,
                                               "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
        to_cart_btn.click()

    def clear_cart(self):
        reset_btn = self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[2]")
        reset_btn.click()
