import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    return page

@pytest.fixture
def cart_data(logged_in_page, request):
    product_choices = getattr(request, "pharm", "1,2,3")
    inventory_page = InventoryPage(logged_in_page)
    total_prod, products = inventory_page.product_count()
    products_data = inventory_page.scrape_products(products, total_prod)
    choices, cart_badge = inventory_page.add_to_cart(products_data, products, total_prod, product_choices)
    return logged_in_page, products_data, choices

@pytest.fixture
def cart_page_ready(cart_data):
    page, products_data, choices = cart_data
    return page
