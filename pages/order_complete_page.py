class CompleteOrderPage:
    def __init__(self, page):
        self.page = page

    def get_confirmation_message(self):
        confirmation = self.page.locator(".complete-header").inner_text()
        return confirmation
        
    def home_page(self):
        self.page.locator('[data-test="back-to-products"]').click()
    