class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url, timeout=30000):
        """Navigate to a URL with an optional timeout."""
        self.page.goto(url, timeout=timeout)

    def click(self, locator, timeout=30000):
        """Click on an element with an optional timeout."""
        self.page.locator(locator).click(timeout=timeout)

    def fill(self, locator, text, timeout=30000):
        """Fill an input field with text."""
        self.page.locator(locator).fill(text, timeout=timeout)

    def is_visible(self, locator, timeout=30000):
        """Check if an element is visible."""
        return self.page.locator(locator).is_visible(timeout=timeout)

    def get_text(self, locator, timeout=30000):
        """Get the inner text of an element."""
        return self.page.locator(locator).inner_text(timeout=timeout)

    def wait_for_element(self, locator, state="visible", timeout=30000):
        """Wait for an element to reach a specific state."""
        self.page.locator(locator).wait_for(state=state, timeout=timeout)

    def scroll_into_view(self, locator, timeout=30000):
        """Scroll an element into view."""
        self.page.locator(locator).scroll_into_view_if_needed(timeout=timeout)