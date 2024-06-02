from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPageClass:
    Click_AppleMacbookPro_Xpath = "//h3[normalize-space()='Apple Macbook Pro']"
    Click_AddtoCart_Button_Xpath = "//input[@value='Add to Cart']"
    Click_ProceedtoCheckout_Button_Xpath = "//a[@class='btn btn-success btn-lg']"
    Text_FirstName_Xpath = "//input[@id='first_name']"
    Text_LastName_Xpath = "//input[@id='last_name']"
    Text_Phone_Xpath = "//input[@id='phone']"
    Text_Address_Xpath = "//textarea[@id='address']"
    Text_ZipCode_Xpath = "//input[@id='zip']"
    Select_State_Xpath = "//select[@id='state']"

    Text_OwnerName_Xpath = "//input[@id='owner']"
    Text_CVV_Xpath = "//input[@id='cvv']"
    Text_CardNumber_Xpath = "//input[@id='cardNumber']"
    Select_ExpirationYear_Xpath = "//select[@id='exp_year']"
    Select_ExpirationMonth_Xpath = "//select[@id='exp_month']"
    Click_Continuetocheckout_Xpath = "//button[@id='confirm-purchase']"
    Validate_Status_Xpath = "//p[@class='lead w-lg-50 mx-auto']"

    def __init__(self, driver):
        self.driver = driver

    def Click_AppleMacbookPro(self):
        self.driver.find_element(By.XPATH, self.Click_AppleMacbookPro_Xpath).click()

    def Click_AddtoCart_Button(self):
        self.driver.find_element(By.XPATH, self.Click_AddtoCart_Button_Xpath).click()

    def Click_ProceedtoCheckout_Button(self):
        self.driver.find_element(By.XPATH, self.Click_ProceedtoCheckout_Button_Xpath).click()

    def Enter_FirstName(self, FirstName):
        self.driver.find_element(By.XPATH, self.Text_FirstName_Xpath).send_keys(FirstName)

    def Enter_LastName(self, LastName):
        self.driver.find_element(By.XPATH, self.Text_LastName_Xpath).send_keys(LastName)

    def Enter_Phone(self, Phone):
        self.driver.find_element(By.XPATH, self.Text_Phone_Xpath).send_keys(Phone)

    def Enter_Address(self, Address):
        self.driver.find_element(By.XPATH, self.Text_Address_Xpath).send_keys(Address)

    def Enter_ZipCode(self, ZipCode):
        self.driver.find_element(By.XPATH, self.Text_ZipCode_Xpath).send_keys(ZipCode)

    def Select_State(self):
        State = Select(driver.find_element(By.NAME, "state"))
        State.select_by_visible_text("Pune")

    def Enter_OwnerName(self, OwnerName):
        self.driver.find_element(By.XPATH, self.Text_OwnerName_Xpath).send_keys(OwnerName)

    def Enter_CVV(self, CVV):
        self.driver.find_element(By.XPATH, self.Text_CVV_Xpath).send_keys(CVV)

    def Enter_CardNumber(self, CardNumber):
        self.driver.find_element(By.XPATH, self.Text_CardNumber_Xpath).send_keys(CardNumber)

    def Select_ExpirationYear(self):
        ExpirationYear = Select(driver.find_element(By.NAME, "exp_year"))
        ExpirationYear.select_by_value("20")

    def Select_ExpirationMonth(self):
        ExpirationMonth = Select(driver.find_element(By.NAME, "exp_year"))
        ExpirationMonth.select_by_value("11")

    def Click_Continuetocheckout(self):
        self.driver.find_element(By.XPATH, self.Click_Continuetocheckout_Xpath).click()

    def Validate_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Validate_Status_Xpath)
            print("Testcase is Passed")
            return "Testcase Passed"
        except:
            print("Testcase is Failed")
            return "Testcase Fail"








