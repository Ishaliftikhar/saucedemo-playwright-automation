import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_complete_page import CompleteOrderPage
from pages.menu_page import MenuPage

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_item")).to_have_count(6)

@pytest.mark.parametrize("username, password, expected_error", [("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"), ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"), ("", "secret_sauce", "Epic sadface: Username is required"), ("standard_user", "", "Epic sadface: Password is required")])
def test_invalid_login(page, username, password, expected_error):

    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login(username, password)
    actual_error = login_page.get_error_message()

    assert actual_error == expected_error

def test_inventory(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    total_prod, products = inventory_page.product_count()

    assert total_prod == 6

def test_product_data(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    total_prod, products = inventory_page.product_count()
    products_data = inventory_page.scrape_products(products, total_prod)
    
    assert len(products_data) == 6

@pytest.mark.parametrize("product_choices", ["1, 2", "1, 2, 3", "4, 5", "2, 4, 6"])
def test_cart(logged_in_page, product_choices):

    inventory_page = InventoryPage(logged_in_page)
    total_prod, products = inventory_page.product_count()
    products_data = inventory_page.scrape_products(products, total_prod)
    choices, cart_badge = inventory_page.add_to_cart(products_data, products, total_prod, product_choices)

    assert len(choices) == int(cart_badge)

@pytest.mark.parametrize("cart_data", ["1, 2", "1, 2, 3", "4, 5", "2, 4, 6"], indirect=True)

def test_cart_products(cart_data):
    page, products_data, choices = cart_data
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_products = cart_page.get_cart_products()

    actual_products = [product["Name"] for product in cart_products]
    expected_products = [products_data[choice-1]["Name"] for choice in choices]

    assert actual_products == expected_products

def test_checkout(cart_page_ready):
    cart_page = CartPage(cart_page_ready)
    cart_page.open_cart()

    checkout_page = CheckoutPage(cart_page_ready)
    checkout_page.checkout()
    checkout_page.fill_info("abcd", "efgh","12345")
    checkout_page.continue_checkout()
    summary = checkout_page.get_summary()

    assert summary["Payment"] == "SauceCard #31337"
    assert summary["Shipping"] == "Free Pony Express Delivery!"

import pytest

@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error", [("", "Khan", "12345", "Error: First Name is required"), ("Ishal", "", "12345", "Error: Last Name is required"), ("Ishal", "Khan", "", "Error: Postal Code is required")])
def test_invalid_checkout(cart_page_ready, first_name, last_name, postal_code, expected_error):
    cart_page = CartPage(cart_page_ready)
    cart_page.open_cart()

    checkout_page = CheckoutPage(cart_page_ready)
    checkout_page.checkout()

    checkout_page.fill_info(first_name, last_name, postal_code)
    checkout_page.continue_checkout()
    actual_error = checkout_page.get_error_message()

    assert actual_error == expected_error
    assert checkout_page.is_on_overview_page() is False


def test_order_completion(cart_page_ready):
    cart_page = CartPage(cart_page_ready)
    cart_page.open_cart()

    checkout_page = CheckoutPage(cart_page_ready)
    checkout_page.checkout()
    checkout_page.fill_info("abcd", "efgh", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_order()

    order_complete_page = CompleteOrderPage(cart_page_ready)
    confirmation = order_complete_page.get_confirmation_message()
    assert confirmation == "Thank you for your order!"

def test_logout(logged_in_page):
    menu_page = MenuPage(logged_in_page)
    menu_page.logout()

    assert logged_in_page.url == "https://www.saucedemo.com/"

