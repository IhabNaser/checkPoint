import re
from playwright.sync_api import Playwright, sync_playwright, expect

from Common import PropsReader
from Models.LoginPage import LoginPage
from Tests.BasicTest import BasicTest

propsReader = PropsReader
expectedTitle = propsReader.main_Page_Title
webpageURL = propsReader.webUrl


class LoginPageTest(BasicTest):

    def __init__(self):
        global loginPage, classInstance
        super().__init__(self)
        loginPage = LoginPage(self.page, webpageURL)
        classInstance = self

    def test_login_sanity(playwright: Playwright, browser=None) -> None:
        if browser is None:
            browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginPage = LoginPage(page, webpageURL)
        username, password, phone = loginPage.get_creds()
        loginPage.login(username, password)
        classInstance.on_finish()

    def test_title(playwright) -> None:
        loginPage.main_page_title(expectedTitle)
        classInstance.on_finish()

    def test_phone_login_sanity(playwright: Playwright) -> None:
        username, password, phone = loginPage.get_creds()
        loginPage.login(phone, password)
        classInstance.on_finish()

    def test_login_with_upper_case(playwright):
        username, password, phone = loginPage.get_creds()
        loginPage.login(username.upper(), password)
        classInstance.on_finish()

    def test_forgot_password(playwright: Playwright) -> None:
        loginPage.forget_password()
        loginPage.screenshot()
        classInstance.on_finish()

    def test_create_account_func(playwright: Playwright) -> None:
        loginPage.create_account_functionality()
        loginPage.screenshot()
        classInstance.on_finish()

    def test_using_guest(playwright: Playwright) -> None:
        loginPage.using_guest()
        classInstance.on_finish()

    def test_login_with_different_browser(self, playwright):
        browser = playwright.webkit.launch(headless=False)
        self.test_login_sanity(playwright, browser)

        classInstance.on_finish()

    def test_main_page_languages(playwright):
        loginPage.main_page_language()
        classInstance.on_finish()

    def test_wrong_username_neg(playwright):
        loginPage.wrong_username()
        classInstance.on_finish()

    def test_wrong_password_neg(playwright):
        loginPage.wrong_password()
        loginPage.screenshot()
        classInstance.on_finish()

    def test_empty_username_neg(playwright):
        loginPage.empty_username()
        classInstance.on_finish()

    def test_empty_password_neg(playwright):
        loginPage.empty_password()
        loginPage.screenshot()
        classInstance.on_finish()

    with sync_playwright() as playwright:
        test_title(playwright)
        test_login_sanity(playwright)
        test_phone_login_sanity(playwright)
        test_login_with_upper_case(playwright)
        test_forgot_password(playwright)
        test_create_account_func(playwright)
        test_using_guest(playwright)
        test_login_with_different_browser(playwright)
        test_main_page_languages(playwright)

        # -------Negative Scenraios-------
        test_wrong_username_neg(playwright)
        test_wrong_password_neg(playwright)
        test_empty_username_neg(playwright)
        test_empty_password_neg(playwright)
