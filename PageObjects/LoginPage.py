from selenium.webdriver.common.by import By


class LoginPageClass:
    Text_LoginPage_Xpath = "//a[normalize-space()='Login']"
    Text_Username_Xpath = "//input[@id='email']"
    Text_Password_Xpath = "//input[@id='password']"
    Click_Login_button_Xpath = "//button[@type='submit']"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"

    def __init__(self, driver):
        self.driver = driver

# conftest driver --> mention testcase --> pageobject method call --> driver mentioned testcase it pointing to that

    def Click_LoginPage_Link(self):
        self.driver.find_element(By.XPATH, self.Text_LoginPage_Xpath).click()

    def Enter_UserEmail(self, UserEmail):
        self.driver.find_element(By.XPATH, self.Text_Username_Xpath).send_keys(UserEmail)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(By.XPATH, self.Click_Login_button_Xpath).click()

    def Validate_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Validate_Status_Xpath)
            print("Testcase is Passed")
            return "Testcase Passed"
        except:
            print("Testcase is Failed")
            return "Testcase Fail"









