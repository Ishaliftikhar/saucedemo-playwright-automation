class CheckoutPage:
    def __init__(self, page):
        self.page = page

    
    def checkout(self): 
        self.page.locator('[data-test="checkout"]').click()

    def fill_info(self, first_name, last_name, postal_code):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)

    def cancel_checkout(self):
        self.page.locator("button#cancel").click()

    def continue_checkout(self):
        self.page.locator('[data-test="continue"]').click()

    def get_summary(self):
        return{"Payment": self.page.locator('[data-test="payment-info-value"]').inner_text(), 
        "Shipping": self.page.locator('[data-test="shipping-info-value"]').inner_text(), 
        "Subtotal" : self.page.locator('[data-test="subtotal-label"]').inner_text(), 
        "Tax" : self.page.locator('[data-test="tax-label"]').inner_text(), 
        "Total" : self.page.locator('[data-test="total-label"]').inner_text()}

    def finish_order(self):
        self.page.locator("#finish").click()

    def cancel_order(self):
        self.page.locator("#cancel").click()

    def get_error_message(self):
        return self.page.locator('[data-test="error"]').inner_text()

    def is_on_overview_page(self):
        return "/checkout-step-two.html" in self.page.url