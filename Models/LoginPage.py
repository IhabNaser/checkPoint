import logging
import re
from playwright.sync_api import Playwright, sync_playwright, expect

from Models.BasicPage import BasicPage


class LoginPage(BasicPage):
    def __init__(self, pageItem, webUrl):
        super().__init__(pageItem, webUrl)

    def forget_password(self):
        expect(self.page.get_by_role(self.propsReader.button, name=self.propsReader.Forgot_email)).to_be_visible()
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.Forgot_email).click()
        expect(self.page.get_by_text(self.propsReader.enter_phone_recovery, exact=True)).to_be_visible()

    def main_page_title(self, expectedTitle):
        expect(self.page).to_have_title(re.compile(self.propsReader.main_Page_Title))

    def create_account_functionality(self):
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.create_account).click()
        self.page.get_by_text(self.propsReader.personal_use).click()
        expect(self.page.get_by_text(self.propsReader.input_name, exact=True)).to_be_visible()
        expect(self.page.get_by_role(self.propsReader.button, name=self.propsReader.next)).to_be_visible()
        self.page.get_by_label(self.propsReader.first_name).click()
        self.page.get_by_label(self.propsReader.first_name).fill(self.propsReader.input_name)
        self.page.get_by_label(self.propsReader.first_name).press(self.propsReader.Tab)
        self.page.get_by_label(self.propsReader.last_name).fill(self.propsReader.input_last_name)
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        self.page.get_by_label(self.propsReader.Month).select_option(self.propsReader.input_month)
        self.page.get_by_label(self.propsReader.Day).fill(self.propsReader.input_day)
        self.page.get_by_label(self.propsReader.Year).fill(self.propsReader.input_year)
        self.page.get_by_label(self.propsReader.Gender, exact=True).select_option("1")
        expect(self.page.get_by_text(self.propsReader.enter_birthday_gender, exact=True)).to_be_visible()
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        self.page.get_by_label(self.propsReader.own_gmail_address).click()
        self.page.get_by_label(self.propsReader.create_gmail_adress).fill(self.propsReader.random_input_mail)
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        expect(self.page.get_by_text(self.propsReader.strong_password, exact=True)).to_be_visible()
        expect(self.page.get_by_role(self.propsReader.button, name=self.propsReader.next)).to_be_visible()

    def using_guest(self):
        expect(self.page.get_by_role(self.propsReader.link, name=self.propsReader.learn_more)).to_be_visible()
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role(self.propsReader.link, name=self.propsReader.learn_more).click()
        page1 = page1_info.value
        expect(page1.get_by_role(self.propsReader.link, name=self.propsReader.google_help)).to_be_visible()
        expect(page1.get_by_role(self.propsReader.heading, name=self.propsReader.chrome_guest)).to_be_visible()

    def main_page_language(self):
        self.page.get_by_label(self.propsReader.english_lang).locator(self.propsReader.div).click()
        self.page.get_by_role(self.propsReader.option, name=self.propsReader.arabic_lang).click()
        expect(self.page.get_by_text(self.propsReader.login_ar, exact=True)).to_be_visible()
        expect(self.page.get_by_label(self.propsReader.expected_ar_lang).locator(self.propsReader.div)).to_be_visible()
        expect(self.page.get_by_role(self.propsReader.button, name=self.propsReader.fogot_mail_ar)).to_be_visible()
        self.page.get_by_label(self.propsReader.expected_ar_lang).locator(self.propsReader.div).click()
        self.page.get_by_role(self.propsReader.option, name=self.propsReader.hebrew_lang).click()
        expect(self.page.get_by_text(self.propsReader.login_he, exact=True)).to_be_visible()
        expect(self.page.get_by_label(self.propsReader.heb_lang_email_phone)).to_be_visible()
        expect(self.page.get_by_label(self.propsReader.heb_lang).locator(self.propsReader.div)).to_be_visible()

    def wrong_username(self):
        self.page.get_by_label(self.propsReader.userSetter).fill(self.propsReader.random_user)
        self.page.get_by_label(self.propsReader.userSetter).press(self.propsReader.control_meta)
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        expect(self.page.get_by_text(self.propsReader.cant_find_account)).to_be_visible()
        expect(self.page.locator(self.propsReader.section)).to_contain_text(self.propsReader.cant_find_account)

    def wrong_password(self):
        username, password, phone = self.get_creds()
        self.page.get_by_label(self.propsReader.userSetter).fill(username)
        self.page.get_by_text(self.propsReader.next_create).click()
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        self.page.get_by_label(self.propsReader.passwordSetter).fill(self.propsReader.wrong_pass)
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        expect(self.page.get_by_text(self.propsReader.wrong_pass_try_again)).to_be_visible()
        expect(self.page.locator(self.propsReader.form)).to_contain_text(self.propsReader.wrong_pass_try_again)
        expect(self.page.get_by_label(username)).to_be_visible()

    def empty_username(self):
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        expect(self.page.get_by_text(self.propsReader.enter_email_phone)).to_be_visible()
        expect(self.page.locator(self.propsReader.section)).to_contain_text(self.propsReader.enter_email_phone)

    def empty_password(self):
        username, password, phone = self.get_creds()
        self.page.get_by_label(self.propsReader.userSetter).fill(username)
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        self.page.get_by_role(self.propsReader.button, name=self.propsReader.next).click()
        expect(self.page.locator(self.propsReader.div).filter(
            has_text=re.compile(r"^Enter a password$")).first).to_be_visible()
        expect(self.page.locator(self.propsReader.form)).to_contain_text(self.propsReader.enter_password)
        expect(self.page.get_by_label(username)).to_be_visible()
