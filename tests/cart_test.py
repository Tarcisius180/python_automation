import time

import pytest
from pages.cart_page import CartPage
class TestCart:
    @pytest.mark.usefixtures("driver")
    def test_add_to_cart_and_checkout(self, data_set, logger):
        cart_page = CartPage(self.driver)
        cart_data = data_set["test_data"]["cart_details"]
        name = cart_data["name"]
        country = cart_data["country"]
        state = cart_data["state"]
        card = cart_data["card"]
        month = cart_data["month"]
        year = cart_data["year"]
        category_url = cart_data['category_url']
        added_text = cart_data['item_added_text']

        logger.info(
            f"Attempting to select a category, a product in the category, enter details for order and getting order number")

        # Navigate to phone category
        cart_page.select_phone_category()
        logger.info(f"Attempting to use {category_url}")
        assert cart_page.verify_page(category_url), "Failed to navigate to phone category"
        logger.info("A category has been selected")

        # Add item to cart
        cart_page.add_item_to_cart()
        time.sleep(3)
        assert cart_page.verify_alert(added_text), "Failed to add item to cart"

        # Go to cart and place order
        cart_page.go_to_cart()
        cart_page.place_order(name, country, state, card, month, year)

        # Verify order confirmation
        time.sleep(3)
        confirmation_text = cart_page.get_order_confirmation()
        order_id = cart_page.get_order_id(confirmation_text)
        assert order_id is not None, "Failed to extract order ID from confirmation"
        print(f"Order placed successfully. Order ID: {order_id}")

        logger.info("Cart test passed")