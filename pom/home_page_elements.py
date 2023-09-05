

class HomePage:

    def __init__(self, page):
        self.header_welcome = page.get_by_text("Welcome")
        self.header_note = page.get_by_text("Fashion You’ll Love")
        self.copyright = page.get_by_text("©2021 by playwright-practice. Proudly created with Wix.com")
        self.login_button = page.get_by_role("button", name="Log In")
