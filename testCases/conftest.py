import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    # initialize the browser namee, options
    if browser=='chrome':
        driver=webdriver.Chrome()
        print(f"Launching {browser} browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print(f"Launching {browser} browser")
    else:
        driver=webdriver.Ie()
    return driver

# command-line interface (CLI) offers a robust and flexible
# allows you to configure various options and behaviors for running your tests.
# get browser name
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #return bw walue to setup method
    return request.config.getoption("--browser")


# pytest html record
# adding enviroment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'francys04'

# for delete/modify env info html report, by default
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

