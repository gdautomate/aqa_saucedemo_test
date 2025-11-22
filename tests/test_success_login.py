import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.success
def test_successful_login(driver):
    login = LoginPage(driver)
    login.load()

    # standard user login
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_logo_visible(), "App logo is not visible. Login may have failed."
