import re
import playwright

class BasicTest:
    """
    Basic class - represents the basic test - all tests should inherit this object
    """
    def __init__(self):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def on_finish(self):
        self.context.close()
        self.browser.close()
        # can add pytest reporting here - didn't use it because i sticked with playwright ONLY .


