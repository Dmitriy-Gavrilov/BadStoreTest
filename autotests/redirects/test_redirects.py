from selenium.webdriver.common.by import By
from autotests.utils import wait_of_element_located
from autotests.cart.test_adding import add_to_cart


def test_redirect_to_home(driver):
    home_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/a[1]")
    home_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/center[1]/h1/font")
    assert page_title.text == "Welcome to BadStore.net!"


def test_redirect_to_catalog(driver):
    catalog_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[1]/a")
    catalog_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/form/h1")
    assert page_title.text == "The following are new items:"


def test_redirect_to_guestbook(driver):
    guestbook_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[2]/a")
    guestbook_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h1")
    assert page_title.text == "Sign our Guestbook!"


def test_redirect_to_orders(driver):
    orders_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[3]/a")
    orders_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h1")
    assert page_title.text == "You have placed the following orders:"


def test_redirect_to_about(driver):
    about_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[4]/a")
    about_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
    assert page_title.text == "About Us!"


def test_redirect_to_account(driver):
    account_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[5]/a")
    account_link.click()
    assert driver.current_url == "http://192.168.31.203/cgi-bin/badstore.cgi?action=myaccount"


def test_redirect_to_login(driver):
    login_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[6]/a")
    login_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h2")
    assert page_title.text == "Login to Your Account or Register for a New Account"


def test_redirect_to_supplier_login(driver):
    supplier_login_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/a[2]")
    supplier_login_link.click()
    page_title = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/h1")
    assert page_title.text == "Welcome Supplier - Please Login:"


def test_redirect_to_supplier_procedures(driver):
    supplier_procedures_link = driver.find_element(By.XPATH,
                                                   "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/a[4]")
    supplier_procedures_link.click()
    page_title = wait_of_element_located(driver, "/html/body/div/p[1]/b/span")
    assert page_title.text == "BadStore.net - Supplier Pricing Upload Procedure"


def test_redirect_to_manual(driver):
    manual_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[8]/a[1]")
    manual_link.click()
    assert driver.current_url == "http://192.168.31.203/BadStore_net_v1_2_Manual.pdf"


def test_redirect_to_cart(driver):
    cart_link = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    cart_link.click()
    page_title = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[3]/font/h1")
    assert page_title.text == "Keep Shopping!"


def test_redirect_to_cart_after_adding(driver):
    catalog_link = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[1]/a")
    catalog_link.click()

    add_to_cart(driver, 2)

    to_cart_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    to_cart_btn.click()

    assert driver.current_url == "http://192.168.31.203/cgi-bin/badstore.cgi?action=cartview"


def test_redirect_to_order(driver):
    catalog_link = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/p[1]/a")
    catalog_link.click()

    add_to_cart(driver, 2)

    to_cart_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[2]/a")
    to_cart_btn.click()

    to_order_btn = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/font/form/center/input[1]")
    to_order_btn.click()

    assert driver.current_url == "http://192.168.31.203/cgi-bin/badstore.cgi?action=submitpayment"
