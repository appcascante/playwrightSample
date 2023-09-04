class HomePage:

    def __init__(self, page):
        self.header = page.get_by_text("Swag Labs")
        self.copyright = page.get_by_text("© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")