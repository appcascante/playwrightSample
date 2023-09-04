import os

import pytest
from playwright.sync_api import Playwright, expect

# import utils.secret_config
from pom.home_pagaitge_elements import HomePage


@pytest.mark.smoke
def test_login_then_logout(set_up) -> None:

    page = set_up

    page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill(utils.secret_config.PASSWORD)
    page.locator("[data-test=\"password\"]").fill(os.environ['PASSWORD'])
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

    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()

def test_check_header(login_set_up) -> None:
    page = login_set_up
    home_page = HomePage(page)

    # page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill("secret_sauce")
    # page.locator("[data-test=\"login-button\"]").click()
    expect(home_page.header).to_be_visible()

    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()