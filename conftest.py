import os

import pytest
from playwright.sync_api import Playwright

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD

# @pytest.fixture(scope="function")
# def set_up(browser):
#     # browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.saucedemo.com/")
#     page.set_default_timeout(30000)
#     # page.goto("")
#     yield page
#     page.close()
#
# @pytest.fixture(scope="function")
# def login_set_up(set_up):
#     # browser = playwright.chromium.launch(headless=False)
#     # context = browser.new_context()
#     # page = context.new_page()
#     # page.goto("https://www.saucedemo.com/")
#     page = set_up
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     yield page

@pytest.fixture()
def set_up(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    # page.goto("")

    yield page

@pytest.fixture()
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://www.saucedemo.com/")
    page = set_up

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill(PASSWORD)
    page.locator("[data-test=\"login-button\"]").click()

    yield page