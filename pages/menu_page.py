class MenuPage:
    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()