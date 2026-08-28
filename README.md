# SauceDemo Playwright Automation

[![SauceDemo Tests](https://github.com/Ishaliftikhar/saucedemo-playwright-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/Ishaliftikhar/saucedemo-playwright-automation/actions/workflows/tests.yml)

This project is a UI automation testing project for the [SauceDemo](https://www.saucedemo.com/) website.

I built this project while learning **Playwright, pytest, and the Page Object Model (POM)**. The main goal was to practice structuring automated tests instead of putting all browser actions directly inside test functions.

## Tech Stack

* Python
* Playwright
* pytest
* pytest-playwright

## Project Structure

```text
Saucedemo/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── order_complete_page.py
│   └── menu_page.py
│
├── tests/
│   └── test_demosauce.py
│
├── utils/
│   └── helpers.py
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Page Objects

The application pages are separated into different Page Object classes.

### LoginPage

Handles:

* Login
* Invalid login error messages

### InventoryPage

Handles:

* Counting products
* Scraping product information
* Adding selected products to the cart

### CartPage

Handles:

* Opening the cart
* Retrieving cart product information

### CheckoutPage

Handles:

* Starting checkout
* Filling customer information
* Continuing checkout
* Reading order summary
* Finishing or cancelling an order
* Checkout validation errors

### CompleteOrderPage

Handles:

* Getting the order confirmation message
* Returning to the products page

### MenuPage

Handles:

* Logging out

## Pytest Fixtures

Reusable setup is kept in `conftest.py`.

### `logged_in_page`

Opens SauceDemo and logs in using the standard test user.

### `cart_data`

Builds on the logged-in fixture, collects product data, and adds selected products to the cart.

The fixture can also be used with indirect parametrization to test different product selections.

### `cart_page_ready`

Uses the cart setup and provides a page with products already added to the cart.

## Parametrization

pytest parametrization is used where the same test needs to be executed with different data.

For example, different product combinations are tested:

```python
@pytest.mark.parametrize(
    "product_choices",
    [
        "1, 2",
        "1, 2, 3",
        "4, 5",
        "2, 4, 6"
    ]
)
```

Invalid login and invalid checkout information are also tested using parametrization.

## Test Coverage

The test suite currently covers:

* Successful login
* Invalid login
* Inventory product count
* Product data extraction
* Adding products to the cart
* Different product combinations
* Cart product verification
* Successful checkout
* Invalid checkout information
* Order completion
* Logout

## Utilities

`utils/helpers.py` contains reusable helper functions.

Currently it includes a function for saving product information to a CSV file.

## Installation

Clone the repository and move into the project directory.

Install the required packages:

```bash
pip install -r requirements.txt
```

Install the Playwright browsers:

```bash
playwright install
```

## Running the Tests

Run the complete test suite:

```bash
pytest
```

Run with more detailed output:

```bash
pytest -v
```

Run the test file directly:

```bash
pytest tests/test_demosauce.py
```

## Test Result

## Test Results

The test suite currently contains 21 tests.

Latest local test run:

`21 passed`

The same test suite is also executed automatically through GitHub Actions on pushes and pull requests.

## Project Approach

The project uses the Page Object Model to keep page-specific browser interactions separate from test logic.

Page Objects are responsible for interacting with the application and returning information.

The test functions are responsible for checking the expected results using assertions.

pytest fixtures are used to avoid repeating common setup such as logging in and preparing products in the cart.

## Future Improvements

Some possible improvements for the project are:

* Add more SauceDemo user scenarios
* Improve browser configuration
* Add screenshots on test failures
* Add HTML test reporting
* Expand test coverage for cart and checkout functionality
