class CartPage:
    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def get_cart_products(self):
        cart_items = self.page.locator(".cart_item")
        total_items = cart_items.count()
    
        cart_products = []
        for n in range(total_items):
            item = cart_items.nth(n)
            name = item.locator(".inventory_item_name").inner_text()
            quantity = item.locator(".cart_quantity").inner_text()
            price = item.locator(".inventory_item_price").inner_text()

            cart_products.append({"Name": name, "Quantity": quantity, "Price": price})
        return cart_products