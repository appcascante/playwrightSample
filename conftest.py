import os
import time

import pytest
# from playwright.sync_api import Playwright

PASSWORD = os.environ['PASSWORD']


@pytest.fixture()
def set_up(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    # page.goto("")

    yield page


@pytest.fixture(scope='session')
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(3000)

    # page.get_by_role("button", name="Log In").click()

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        page.wait_for_load_state('networkidle')

    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("test12345@gmail.com")
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    time.sleep(2)
    context.storage_state(path='state.json')

    yield context
    time.sleep(5)


@pytest.fixture()
def login_set_up(context_creation, browser):
    # context = context_creation
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill(PASSWORD)
    # page.locator("[data-test=\"login-button\"]").click()
    #
    # time.sleep(2)
    # context.storage_state(path='state.json')

    yield page
    context.close()
