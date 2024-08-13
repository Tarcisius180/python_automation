import pytest


def assert_page_url(page_object, expected_url, logger):
    logger.info(f"Verifying navigation to URL: {expected_url}")
    assert page_object.verify_page(expected_url), f"Failed to navigate to URL: {expected_url}"
    logger.info(f"Successfully navigated to URL: {expected_url}")


def assert_alert_text(page_object, expected_text, logger):
    logger.info(f"Verifying alert with text: {expected_text}")
    assert page_object.verify_alert(expected_text), f"Failed to verify alert with text: {expected_text}"
    logger.info(f"Successfully verified alert with text: {expected_text}")


def assert_order_id_extracted(order_id, logger):
    logger.info("Verifying order ID extraction")
    assert order_id is not None, "Failed to extract order ID from confirmation"
    logger.info(f"Successfully extracted order ID: {order_id}")
