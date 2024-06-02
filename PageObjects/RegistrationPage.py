
from selenium.webdriver.common.by import By



class RegistrationClass:
    Click_RegistrationPage_Xpath = "//a[normalize-space()='Register']"
    Text_Name_Xpath = "//input[@id='name']"
    Text_Email_Xpath = "//input[@id='email']"
    Text_Password_Xpath = "//input[@id='password']"
    Text_ConfirmPassword_Xpath = "//input[@id='password-confirm']"
    Click_Register_button_Xpath = "//button[@type='submit']"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"

    def __init__(self, browser):
        self.browser = browser

    def Click_RegistrationPage_Link(self):
        self.browser.find_element(By.XPATH, self.Click_RegistrationPage_Xpath).click()

    def Enter_Name(self, Name):
        self.browser.find_element(By.XPATH, self.Text_Name_Xpath).send_keys(Name)

    def Enter_Email(self, Email):
        self.browser.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(Email)

    def Enter_Password(self, password):
        self.browser.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Enter_ConfirmPassword(self, ConfirmPassword):
        self.browser.find_element(By.XPATH, self.Text_ConfirmPassword_Xpath).send_keys(ConfirmPassword)

    def Click_Register_button(self):
        self.browser.find_element(By.XPATH, self.Click_Register_button_Xpath).click()

    def Validate_Status(self):
        try:
            self.browser.find_element(By.XPATH, self.Validate_Status_Xpath)
            print("Login Testcase is Passed")
            return "Testcase Passed"
        except:
            print("Login Testcase is Failed")
            return "Testcase Fail"





















