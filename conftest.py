import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime

BASE_URL = "https://www.saucedemo.com/"

def _create_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def driver(request):
    """Provides WebDriver and captures screenshot on failure."""
    headless = os.environ.get("HEADLESS", "1") != "0"
    driver = _create_driver(headless=headless)
    yield driver

    # Screenshot if test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)
        filename = f"reports/{request.node.name}_failure.png"
        driver.save_screenshot(filename)

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
