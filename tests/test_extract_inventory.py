import pytest
import json
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.extract
def test_extract_inventory(driver):
    login = LoginPage(driver)
    login.load()

    # Login as standard user
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    # Extract data
    items = inventory.get_all_items()

    # Save to file (reports folder)
    os.makedirs("reports", exist_ok=True)
    file_path = "reports/inventory_data.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

    assert os.path.exists(file_path), "Data file was not created"
    assert len(items) > 0, "No items extracted from inventory page"

    # Logout
    inventory.logout()

    # Verify back on login page
    assert "saucedemo.com" in driver.current_url and "inventory" not in driver.current_url
