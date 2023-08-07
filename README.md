
## Selenium-Hybrid-Frame
A Selenium hybrid framework for web automation is a comprehensive approach that combines various design patterns, techniques, and tools to create a structured and maintainable automation solution for testing web applications. It leverages the strengths of different frameworks and methodologies to achieve efficient test automation. 
I try to test the nopCommerce.com site but you can test any site with this project. Here's a detailed description of a Selenium hybrid framework for web automation:

### Project Description: Selenium Hybrid Framework for Web Automation
- Overview:
- The Selenium hybrid framework for web automation is designed to provide a modular, scalable, and robust solution for automating the testing of web applications. It combines the strengths of various frameworks, including data-driven, keyword-driven, and page object models, to create a flexible and maintainable automation solution.

### Install packages
All packages you can see in dir project (pip isntall) file:
- Selenium 
- Pytest
- Pytest-html
- Pytest-xdist
- Openpyxl: MS Excell supported
- Allure-pytest
#### Key Components and Features:
- Modular Architecture:
The framework is organized into modular components, allowing testers to work on specific parts of the application independently. Each module can represent a set of related test cases or functionalities.

#### Page Object Model (POM):
- LoginPage.py -> test login page as administrator on nonCommerce
- The POM design pattern is utilized to create a separate class for each web page or component of the application. These classes encapsulate the locators and methods for interacting with the page elements. This ensures better reusability and maintainability.

#### Data-Driven Testing:
- The framework supports data-driven testing, where test data is stored in external data sources such as Excel, CSV, or databases. Test scripts are designed to read test data from these sources, allowing testers to run the same test scenario with different data sets.
- Import Excell file and create XLUtilities.py with Openpyxl and create clone test 1 to test 2.
- In excell file we will have tabel with next columns: username, passw, exp and lst. Run this in terminal `pytest -s -v --html = Reports\report-html` -> (-s: for version under 3.0.0 use without -s). 
- Programm do next executions: 
1. login in with correct username, and pass
2. after logout and put incorrect username and password and compare with exp data, progaramm decide (Fail or Pass)
#### Grouping tests
1. @pytest.merk.sanity
2. @pytest.mark.regression
Craete pytest.ini to specify groups of tests
- Run this command in terminal:
`pytest -v -m 'sanity and regression' --html = ./Reports/report.html testCases/ --browser chrome`


#### Keyword-Driven Testing:
- Keyword-driven testing allows testers to create test scripts using keywords or actions that represent specific interactions with the application. Testers can define custom keywords that abstract complex actions, making test scripts more readable and reusable.
- I also add new tests after first tests with another cases like:
1. add new custommer
2. search custommer by email
3. serach custommer by name
All of these put into AddcustommerPage.py (Page Object) and test_addCustommer.py
- Test existing custommer check -> SerachCustommerPage.py (email and name)

#### Centralized Configuration:
- Configuration settings such as URLs, browser types, timeouts, and other parameters are stored in a centralized configuration file. This allows testers to easily update configuration settings without modifying the test scripts.

#### Logging and Reporting:
- The framework integrates logging and reporting mechanisms to provide detailed information about test execution. Logs capture step-by-step actions and results, while comprehensive reports offer insights into test coverage and outcomes.

#### Cross-Browser and Cross-Platform Testing:
- The framework supports cross-browser and cross-platform testing by allowing testers to specify the target browser and platform for test execution. This ensures compatibility and consistent behavior across different environments.

#### Screenshot Capture:
- Screenshots are automatically captured during test execution, helping testers visually verify the application's state at different stages. Screenshots are organized and stored for reference.

#### Test Data Management:
- The framework includes utilities for managing test data, including data extraction, transformation, and loading. This is particularly useful for scenarios involving large datasets.

#### Parallel Execution:
- Parallel test execution is supported, enabling faster testing cycles by running multiple tests simultaneously across different browsers or environments.

### Benefits:
- Improved Test Maintenance: The modular and organized structure of the framework simplifies test maintenance and updates.
- Reusability: Components such as page objects and keywords can be reused across different test scenarios.
- Scalability: New test cases and functionalities can be added easily by extending existing modules.
- Enhanced Collaboration: The framework's standardized structure facilitates collaboration among team members.
- Reliable Testing: The combination of data-driven, keyword-driven, and POM approaches ensures comprehensive and reliable testing.
### Conclusion:
- The Selenium hybrid framework for web automation is a comprehensive solution that combines the strengths of various automation techniques to create a flexible, maintainable, and efficient testing environment for web applications. It promotes best practices, enhances test coverage, and improves the overall quality of software products by automating repetitive testing tasks.