import pytest
from pages.login_page import LoginPage

@pytest.mark.failed
def test_failed_login(driver):
    login = LoginPage(driver)
    login.load()

    # locked out user
    login.login("locked_out_user", "secret_sauce")

    error_text = login.get_error_message()

    # PDF expects “Sorry, this user has been banned.”
    assert "banned" in error_text.lower() or "locked out" in error_text.lower(), \
        f"Expected ban error but got: {error_text}"
