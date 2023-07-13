import pytest
from selenium import webdriver
# call login page
from pageObjects.LoginPage import Login
from testCases.conftest import setup
# call readProprietes/utilities for url, username and passw data from ini file
from utilities.readProperties import ReadConfig
# call customLog/utilities for error data messages from pytest
from utilities.customLogger import LogGen

# create test class
class Test_001_Login:
    # insert url, username and passw
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # for log meesages
    logger=LogGen.loggen()

    # test page home
    def test_homePageTitle(self, setup):
        # for log messages
        self.logger.info("########Test_001_Login########")
        self.logger.info("########Verify Home Page Title########")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        # check title of the page
        if act_title=="Your store. Login":
            assert True
            # if all passed close browser
            self.logger.info("########Home page title test is passed########")
            self.driver.close()
        else:
            # for capture error, .\\=> represent current project
            self.logger.error("########Home page title test is failed########")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

#     test login
    def test_login(self, setup):
        self.logger.info("########Verify login test########")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassw(self.password)
        self.lp.clickLogin()
#         validation of login
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("########Login test is passed########")
            self.driver.close()
            assert True
        else:
            self.logger.error("########Login test is failed########")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()

            assert False





