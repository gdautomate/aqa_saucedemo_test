from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username)
        ).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_msg)
            ).text
        except:
            return ""
