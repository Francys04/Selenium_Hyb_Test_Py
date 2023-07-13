import pytest
from selenium import webdriver
# call login page
from pageObjects.LoginPage import Login
from testCases.conftest import setup
# call readProprietes/utilities for url, username and passw data from ini file
from utilities.readProperties import ReadConfig
# call customLog/utilities for error data messages from pytest
from utilities.customLogger import LogGen
# call xlutilies/utilies for excell file
from utilities import XLUtils
# time to sleep operation after click login
import time


# create test class
class Test_002_DDT_Login:
    # insert url, username and passw
    baseURL = ReadConfig.getApplicationURL()
    path="./TestData/test_data.xlsx"
    # for log meesages
    logger=LogGen.loggen()

    # test page home


#     test login
    def test_login_ddt(self, setup):
        self.logger.info("########Test_002_DDT_Login#######")
        self.logger.info("########Verify login test########")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        # get data from excell file
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print(f"Number of rows in excell: {self.rows}")


        lst_status=[] #entry list variable

        # read frow rows data in excell
        for row in range(2, self.rows+1):
            self.user=XLUtils.readData(self.path, "Sheet1", row,1)
            self.password = XLUtils.readData(self.path, "Sheet1", row, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", row, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassw(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            # for validation to login
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            #verify
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    # append in list when test pass with correct data login
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")

#                 verify if exist exp fail and pass
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");




