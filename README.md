# SauceDemo Playwright Automation Framework

A UI automation testing framework for the SauceDemo web application using **Python, Playwright, and pytest**.

The project follows the **Page Object Model (POM)** design pattern and uses pytest fixtures and parametrization to create reusable and maintainable automated tests.

## Tech Stack

* Python
* Playwright
* pytest
* pytest-playwright
* Page Object Model (POM)

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
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
├── utils/
│   └── helpers.py
```

## Page Objects

Each major application page has its own Page Object class.

* `LoginPage` - Login and login error handling
* `InventoryPage` - Product retrieval and adding products to the cart
* `CartPage` - Opening the cart and retrieving cart products
* `CheckoutPage` - Checkout, customer information, order summary, and validation
* `CompleteOrderPage` - Order confirmation and returning to products
* `MenuPage` - Logout functionality

## Test Coverage

The test suite covers:

* Valid login
* Invalid login scenarios
* Inventory product count
* Product data extraction
* Adding products to cart
* Multiple cart combinations
* Cart product verification
* Successful checkout
* Invalid checkout information
* Order completion
* Logout

## Pytest Fixtures

Reusable fixtures are defined in `conftest.py`.

### `logged_in_page`

Opens SauceDemo and logs in using the standard test account.

### `cart_data`

Builds on `logged_in_page`, retrieves product data, and adds the selected products to the cart.

The fixture supports indirect parametrization for testing different product combinations.

### `cart_page_ready`

Builds on `cart_data` and provides a page that is already prepared with products in the cart.

## Parametrization

pytest parametrization is used to test multiple scenarios without duplicating test functions.

For example, different product combinations can be tested:

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

Invalid login and checkout scenarios are also parametrized.

## Installation

Clone the repository and navigate to the project directory.

Install the required Python packages:

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

Run tests with detailed output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_demosauce.py
```

## Test Results

Current test suite:

**21 tests passed**

```text
21 passed
```

## Design Approach

The framework separates responsibilities between Page Objects and test cases.

### Page Objects

Page Objects handle:

* Locators
* UI interactions
* Extracting information from pages

### Tests

Tests handle:

* Test scenarios
* Test data
* Assertions
* Parametrization

This separation makes the test suite easier to maintain and extend.

## Future Improvements

Potential future improvements include:

* Browser configuration through pytest options
* Additional SauceDemo user scenarios
* Screenshot capture on failures
* HTML test reporting
* CI/CD integration
* Additional page workflows
|
