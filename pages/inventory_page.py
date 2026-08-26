class InventoryPage:

    def __init__(self, page):
        self.page = page

    def product_count(self):
        products = self.page.locator("div.inventory_item")
        total_prod = products.count()

        return total_prod , products

    def scrape_products(self, products, total_prod):
        products_data = []
        for n in range(total_prod):
            product = products.nth(n)
            product_name = product.locator(".inventory_item_name").inner_text()
            product_desc = product.locator(".inventory_item_desc").inner_text()
            product_price = product.locator(".inventory_item_price").inner_text()
            products_data.append({"Name" : product_name, "Description" : product_desc, "Price" : product_price})

        return products_data

    def add_to_cart(self, products_data, products, total_prod, choices):
        
        choices = [int(choice.strip()) for choice in choices.split(",")]
        if any(choice < 1 or choice > total_prod for choice in choices):
            raise ValueError(f"Product choices must be between 1 and {total_prod}.")
        choices = list(dict.fromkeys(choices))

        for choice in choices:
            product = products.nth(choice - 1)
            product.locator("button").click()

        cart_badge = self.page.locator("span.shopping_cart_badge").inner_text()

        return choices, cart_badge
    