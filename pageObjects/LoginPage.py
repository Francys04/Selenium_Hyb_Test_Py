# page object class
from selenium import webdriver

class Login:
    # loginpage locators, id from inspect html
    text_username_id="Email"
    # for passw
    text_passw_id="Password"
    # butt for login
    button_login_xpath="//button[contains(text(),'Log in')]"
    # linktext for logout
    link_logout_linktext="Logout"

    # controction for object creation, driver=class var
    def __init__(self, driver):
        self.driver=driver

    # actions for set username
    def setUserName(self, username):
        # clear data space
        self.driver.find_element_by_id(self.text_username_id).clear()
        # set username
        self.driver.find_element_by_id(self.text_username_id).send_keys(username) #selenium webdriver

    # actions for password
    def setPassw(self, password):
        self.driver.find_element_by_id(self.text_passw_id).clear()
        self.driver.find_element_by_id(self.text_passw_id).send_keys(password)

    # click action button for login
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    # click logout
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
