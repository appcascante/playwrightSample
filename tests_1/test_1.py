import pytest
from playwright.sync_api import expect
# import utils.secret_config
from pom.home_page_elements import HomePage


@pytest.mark.smoke
@pytest.mark.parametrize("username", ["standard_user", "performance_glitch_user", "problem_user",
                                      pytest.param("locked_out_user", marks=pytest.mark.xfail)])
def test_login_then_logout(set_up, username) -> None:
    page = set_up

    page.locator("[data-test=\"username\"]").fill(username)
    # page.locator("[data-test=\"password\"]").fill(utils.secret_config.PASSWORD)
    # page.locator("[data-test=\"password\"]").fill(PASSWORD)
    page.fill("[data-test=\"password\"]", "secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()


def test_check_copyright(login_set_up) -> None:
    page = login_set_up
    home_page = HomePage(page)

    # page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill("secret_sauce")
    # page.locator("[data-test=\"login-button\"]").click()
    # page.get_by_text("© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy").click()

    expect(home_page.copyright).to_be_visible()
    # assert page.is_visible(home_page.copyright)

    # page.get_by_role("button", name="Open Menu").click()
    # page.get_by_role("link", name="Logout").click()


def test_check_header(login_set_up) -> None:
    page = login_set_up
    home_page = HomePage(page)

    # page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill("secret_sauce")
    # page.locator("[data-test=\"login-button\"]").click()

    expect(home_page.header_welcome).to_be_visible()
    expect(home_page.header_note).to_be_visible()

    # page.get_by_role("button", name="Open Menu").click()
    # page.get_by_role("link", name="Logout").click()
