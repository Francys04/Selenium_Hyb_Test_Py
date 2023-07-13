# create a class, for verify existing users
class SearchCustomer():
    # Add customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"

    # xpath of grid table of all users
    tblSearchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr" #rows table
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td" #columns of table

    # define constructor for driver
    def __init__(self, driver):
        self.driver = driver
    # set email, clear and after put located email_id(from table), not random
    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email) #email from table
    # set first name
    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)
    # set lastname
    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)
    # check with click buttom search
    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()
    # get number of rows
    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
    # number of columns, written number of columns
    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))
    # validation from pass email_id
    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag
    # for username
    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag