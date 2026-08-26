class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

    def get_error_message(self):
        return self.page.locator('[data-test="error"]').inner_text()