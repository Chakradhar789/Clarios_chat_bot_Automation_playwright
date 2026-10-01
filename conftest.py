import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page(
            viewport={
                "width": 1440,
                "height": 600
            }
        )

        # Maximum time for element actions
        page.set_default_timeout(120000)

        # Maximum time for navigation
        page.set_default_navigation_timeout(120000)

        yield page

        browser.close()