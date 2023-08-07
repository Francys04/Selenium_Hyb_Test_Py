import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustommerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassw(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by nameID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
        self.driver.close()
        
        
"""The test is related to a web application's customer management system. Here's a breakdown of what the code does:

Import Statements:
The code imports various modules and classes necessary for running the test case, 
including time, pytest, and different page object classes (Login, AddCustomer, SearchCustomer) 
as well as utility modules (ReadConfig and LogGen).

Test Class Definition:
The code defines a test class named Test_SearchCustomerByName_005 that contains the test methods.

Test Data Setup:
The test class defines class-level variables such as baseURL, username, 
and password by reading them from a configuration file using the ReadConfig utility.

Logger Setup:
A logger is set up using the LogGen class to log messages during the test execution.

Test Method Definition:
The code defines a test method named test_searchCustomerByEmail. This method is 
decorated with @pytest.mark.regression to categorize it as a regression test.

Test Setup (setup Fixture):
The method takes a parameter setup, which is a fixture provided by the testing framework 
to set up the test environment. Within the method, the logger is used to log relevant information.

Test Steps:

The test method opens a web browser, navigates to the application's URL, and logs in using the 
provided username and password.
It then logs a successful login message and proceeds to search for a customer by name.
The AddCustomer page object is used to navigate to the customer management section and initiate a search.
The SearchCustomer page object is used to set the first name and last name fields for 
the search and then click the search button.
The time.sleep(5) pause is used to wait for the search results to load.
The searchCustomerByName method is used to verify if the search results match the provided customer name. 
The result is then asserted to be True.
Test Teardown:
After the test steps are completed, the driver is closed, and the test method finishes.

Overall, this code seems to be a part of an automated testing framework using the PyTest library to test 
the functionality of searching for a customer by name and email in a web application's customer management system. 
It follows the Page Object Model design pattern to separate the test logic from the web page interactions."""