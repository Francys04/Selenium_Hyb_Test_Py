"""For writing and running tests in Python."""
import pytest
"""Provides various time-related functions."""
import time
"""Login from the LoginPage module (file) in the pageObjects package. """
from pageObjects.LoginPage import Login
"""Similar to the previous import, this line imports a class 
named AddCustomer from the AddCustommerPage module in the pageObjects package."""
from pageObjects.AddCustommerPage import AddCustomer
"""This imports a class named ReadConfig from the readProperties module in the utilities package. 
This is utility class for reading configuration properties."""
from utilities.readProperties import ReadConfig
"""This imports a class named LogGen from the customLogger module in the utilities package. 
This is a custom logging utility for your test framework."""
from utilities.customLogger import LogGen
"""This imports the built-in string module, which provides various functions 
and constants related to strings."""
import string
"""This imports the built-in random module, which is used for generating 
random numbers or making random selections."""
import random


class Test_003_AddCustomer:
    # insert url, username and passw
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # for log meesages
    logger=LogGen.loggen()
    # add decorators
    @pytest.mark.sanity

    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window() #maximize window of chrome bw

        # login page elements
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassw(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        # set personal data
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Alex")
        self.addcust.setLastName("Morohai")
        self.addcust.setDob("4/06/1997")  # Format: D / MM / YYY
        self.addcust.setCompanyName("francys04")
        self.addcust.setAdminContent("Testing")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        # print info that custommer add succesufully, capture with screenshot
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

#generate random data, user defined function, data with upper and low case, 8 char
# generate 8 characters and concatinated with @gmail.com
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

"""Test_003_AddCustomer defines a test scenario using the pytest testing framework. 
This class appears to be a part of a larger test suite for automating the testing of adding 
a customer to a web application. Here's a breakdown of what the code is doing:

The class Test_003_AddCustomer is defined, presumably for testing the functionality of adding a customer.

The class defines class-level variables baseURL, username, and password, which are read from configuration using ReadConfig.

The class also sets up logging using the LogGen.loggen() method.

The @pytest.mark.sanity decorator is applied to the test method test_addCustomer, 
indicating that this test is part of the "sanity" category.

The test_addCustomer method is defined, which contains the actual test logic.

The test method performs the following steps:

Initializes the web driver by using the setup fixture.
Navigates to the specified base URL.
Logs into the application using the provided username and password.
Navigates to the customer management section and starts adding a new customer.
Provides various customer details, including generating a random email address.
Validates the success message after adding the customer and takes appropriate actions based on the validation result.
Closes the browser.
The random_generator function is defined to generate random data (8 characters, lowercase letters, and digits) 
for creating a random email address."""