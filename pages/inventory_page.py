from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    logo = (By.CLASS_NAME, "app_logo")
    items = (By.CLASS_NAME, "inventory_item")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def is_logo_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logo)
        ).is_displayed()

    def get_all_items(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.items)
        )
        data = []
        products = self.driver.find_elements(*self.items)

        for item in products:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            desc = item.find_element(By.CLASS_NAME, "inventory_item_desc").text

            data.append({
                "title": title,
                "price": price,
                "description": desc
            })

        return data

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
