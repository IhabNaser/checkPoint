from jproperties import Properties
import logging
import re
from playwright.async_api import expect
import datetime
from Common import PropsReader


class BasicPage:
    """
    Basic Page - represents a base page for all pages in the project
     methods:
      1. login
      2. validate_login_success
      3. screenshot
      4. get_creds
    """

    def __init__(self, pageitem, webUrl):
        self.page = pageitem
        self.page.goto(webUrl)
        self.propsReader = PropsReader

    def login(self, user, password):
        logging.info("login using user: " + user + "and password: " + password)
        self.page.get_by_label(self.propsReader.userSetter).click()
        self.page.get_by_label(self.propsReader.userSetter).fill(user)
        self.page.get_by_role(self.propsReader.buttonSetter, name="Next").click()
        self.page.get_by_label(self.propsReader.passwordSetter).click()
        self.page.get_by_label(self.propsReader.passwordSetter).fill(password)
        self.page.get_by_role("button", name="Next").click()
        self.screenshot()
        self.validate_login_success()

    def validate_login_success(self):
        expect(self.page.get_by_role(self.propsReader.navigationSetter).locator("div").filter(
            has_text=re.compile(r"^Inbox$")).nth(
            3)).to_be_visible()
        expect(self.page.get_by_role(self.propsReader.navigationSetter).locator("div").filter(
            has_text=re.compile(r"^Starred$")).nth(
            3)).to_be_visible()
        expect(self.page.get_by_role("link", name="Gmail", exact=True)).to_be_visible()

        def readProp(self):
            configs = Properties()

            with open('../Properties/app-props.properties', 'rb') as config_file:
                configs.load(config_file)

            print(configs.get("DB_User"))
            # PropertyTuple(data='root', meta={})

            print(f'Database User: {configs.get("DB_User").data}')
            # Database User: root

            print(f'Database Password: {configs["DB_PWD"].data}')
            # Database Password: root@neon

    def screenshot(self):
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d-%H-%M-%S") + '.png'
        fullfileName = self.propsReader.screenshotsPath + '/' + filename
        logging.info("Taking a snap as screenshot in :" + fullfileName)
        return self.page.screenshot(path=fullfileName)

    def get_creds(self):
        # Make it before annotation
        f = open(self.propsReader.loginCredsPath, "r")
        username = f.readline().split(self.propsReader.userLine)[1].strip()
        phone = f.readline().split(self.propsReader.phoneLine)[1].strip()
        password = f.readline().split(self.propsReader.passLine)[1].strip()
        return username, password, phone
