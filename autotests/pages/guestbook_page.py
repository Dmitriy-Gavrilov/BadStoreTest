from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class GuestbookPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_note_to_guestbook(self, note: str):
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/center/textarea").send_keys(note)
        self.driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/form/center/input[2]").click()
