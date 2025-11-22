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
        from selenium.common.exceptions import TimeoutException
        logout_xpath = "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]"

        # Click the menu button using JavaScript
        try:
            menu_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.menu_button)
            )
            self.driver.execute_script("arguments[0].click();", menu_btn)
        except TimeoutException:
            btn = self.driver.find_element(*self.menu_button)
            self.driver.execute_script("arguments[0].click();", btn)

        # Wait for logout to appear using your full XPath
        try:
            logout_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, logout_xpath))
            )
        except TimeoutException:
            # Retry by refreshing and clicking menu again
            self.driver.refresh()
            menu_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.menu_button)
            )
            self.driver.execute_script("arguments[0].click();", menu_btn)

            logout_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, logout_xpath))
            )

        # Click logout using JavaScript
        self.driver.execute_script("arguments[0].click();", logout_btn)

