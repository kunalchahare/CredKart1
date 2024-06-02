# # import pytest
# # from selenium.webdriver.common.by import By
# import random
# import string
#
# from PageObjects.LoginPage import LoginPageClass
# from PageObjects.RegistrationPage import RegistrationClass
#
# # @pytest.mark.usefixtures("setup")
# class Test_UserProfile:
#
#     def test_UserLogin001(self, setup):
#         # driver = webdriver.Chrome()
#         # driver.maximize_window()
#         # driver.get("https://automation.credence.in/login")
#         # time.sleep(2)
#
#         self.driver = setup                        # this is the fixture captured from conftest
#         self.lp = LoginPageClass(self.driver)      # import page object class
#
#         # self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#         self.lp.Click_LoginPage_Link()
#
#         # self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
#         self.lp.Enter_Username("Credencetest@test.com")
#
#         # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
#         self.lp.Enter_Password("Credence@123")
#
#         # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         self.lp.Click_LoginButton()
#
#         # try:
#         #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
#         #     print("Login Testcase is Passed")
#         # except:
#         #     print("Login Testcase is Failed")
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Pass.png")
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Fail.png")
#             assert False
#
#
#
#     def test_UserRegistration002(self, setup):
#         self.driver = setup
#         self.rp = RegistrationClass(self.driver)
#         self.lp = LoginPageClass(self.driver)
#
#         self.rp.Click_RegistrationPage_Link()
#         self.rp.Enter_Name("Payal")
#         self.rp.Enter_Email("cbm@abc.com")
#         self.rp.Enter_Password(111213)
#         self.rp.Enter_ConfirmPassword(111213)
#         self.rp.Click_Register_button()
#
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")   # (C:\Users\hp\PycharmProjects\Credkart_Pytest\Screenshots)
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")
#             assert False




        # Credkart Login And Registration Testcase with Random Email Generator And Replacing Hard Core Values #

# # import pytest
# # from selenium.webdriver.common.by import By
# import random
# import string
#
# from PageObjects.LoginPage import LoginPageClass
# from PageObjects.RegistrationPage import RegistrationClass
# from Utilities.readConfigFile import Readconfig
#
# class Test_UserProfile:
#
#     UserEmail = Readconfig.getUserEmail()   #U serEmail = Credencetest@test.com
#     Password = Readconfig.getPassword()     # Password = Credence@123
#
#     def test_UserLogin001(self, setup):
#
#         self.driver = setup  # this is the fixture captured from conftest
#         self.lp = LoginPageClass(self.driver)  # import page object class
#
#         self.lp.Click_LoginPage_Link()
#
#         self.lp.Enter_Username(self.UserEmail)
#         print("UserEmail:", self.UserEmail)
#
#         self.lp.Enter_Password(self.Password)
#         print("Password:", self.Password)
#
#         self.lp.Click_LoginButton()
#
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Pass.png")
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Fail.png")
#             assert False
#
#     def test_UserRegistration002(self, setup):
#         self.driver = setup
#         self.rp = RegistrationClass(self.driver)
#         self.lp = LoginPageClass(self.driver)
#
#         self.rp.Click_RegistrationPage_Link()
#         self.rp.Enter_Name("Payal")
#
#         email = Generate_Email()
#         self.rp.Enter_Email(email)
#         print(email)
#
#         self.rp.Enter_Password(111213)
#         self.rp.Enter_ConfirmPassword(111213)
#         self.rp.Click_Register_button()
#
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot(
#                 "..\\Screenshots\\test_UserRegistration002.png")  # (C:\Users\hp\PycharmProjects\Credkart_Pytest\Screenshots)
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")
#             assert False
#
#
# def Generate_Email():
#     username = ''.join(random.choices(string.ascii_lowercase, k=3))  # random 3 char lower case  e.g. abc
#     domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
#     return f"{username}@{domain}"  # random 3 char + domain





#         # Logs #
#
# # import pytest
# # from selenium.webdriver.common.by import By
# import random
# import string
#
# from PageObjects.LoginPage import LoginPageClass
# from PageObjects.RegistrationPage import RegistrationClass
# from Utilities.readConfigFile import Readconfig
# from Utilities.Logger import LogGenerator
#
# class Test_UserProfile:
#
#     UserEmail = Readconfig.getUserEmail()   #U serEmail = Credencetest@test.com
#     Password = Readconfig.getPassword()     # Password = Credence@123
#     log = LogGenerator.loggen()
#
#     def test_UserLogin001(self, setup):
#
#         self.log.warning("This is warning")
#         self.log.info("This is info")
#         self.log.error("This is error")
#         self.log.critical("This is critical")
#
#         self.driver = setup  # this is the fixture captured from conftest
#         self.lp = LoginPageClass(self.driver)  # import page object class
#
#         self.lp.Click_LoginPage_Link()
#
#         self.lp.Enter_Username(self.UserEmail)
#         print("UserEmail:", self.UserEmail)
#
#         self.lp.Enter_Password(self.Password)
#         print("Password:", self.Password)
#
#         self.lp.Click_LoginButton()
#
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Pass.png")
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Fail.png")
#             assert False
#
#     def test_UserRegistration002(self, setup):
#         self.driver = setup
#         self.rp = RegistrationClass(self.driver)
#         self.lp = LoginPageClass(self.driver)
#
#         self.rp.Click_RegistrationPage_Link()
#         self.rp.Enter_Name("Payal")
#
#         email = Generate_Email()
#         self.rp.Enter_Email(email)
#         print(email)
#
#         self.rp.Enter_Password(111213)
#         self.rp.Enter_ConfirmPassword(111213)
#         self.rp.Click_Register_button()
#
#         if self.lp.Validate_Status() == "Testcase Passed":
#             self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")  # (C:\Users\hp\PycharmProjects\Credkart_Pytest\Screenshots)
#             assert True
#         else:
#             self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")
#             assert False
#
#
# def Generate_Email():
#     username = ''.join(random.choices(string.ascii_lowercase, k=3))  # random 3 char lower case  e.g. abc
#     domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
#     return f"{username}@{domain}"  # random 3 char + domain



        # RUNNING PYTEST WITH REQUIRED BROWSER WITH COMMAND #

# import pytest
# from selenium.webdriver.common.by import By
import random
import string

from PageObjects.LoginPage import LoginPageClass
from PageObjects.RegistrationPage import RegistrationClass
from Utilities.readConfigFile import Readconfig
from Utilities.Logger import LogGenerator


class Test_UserProfile:

    UserEmail = Readconfig.getUserEmail()   # UserEmail = Credencetest@test.com
    Password = Readconfig.getPassword()     # Password = Credence@123
    log = LogGenerator.loggen()

    def test_UserLogin001(self, setup):

        self.log.info("Testcase test_UserLogin001 is Started")
        self.log.info("Opening Browser")
        self.driver = setup  # this is the fixture captured from conftest
        self.lp = LoginPageClass(self.driver)  # import page object class

        self.log.info("Click on Login Page Link")
        self.lp.Click_LoginPage_Link()

        self.lp.Enter_UserEmail(self.UserEmail)
        self.log.info("Enter Username:" + self.UserEmail)
        print("UserEmail:", self.UserEmail)

        self.lp.Enter_Password(self.Password)
        self.log.info("Enter Password:" + self.Password)
        print("Password:" + self.Password)

        self.lp.Click_LoginButton()
        self.log.info("Click on Login Button")

        if self.lp.Validate_Status() == "Testcase Passed":
            self.log.info("Testcase test_UserLogin001 is Passed")
            self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Pass.png")
            assert True
        else:
            self.log.info("Testcase test_UserLogin001 is Failed")
            self.driver.save_screenshot("..\\Screenshots\\test_UserLogin001_Fail.png")
            assert False

        self.log.info("Testcase test_UserLogin001 is Completed")

    def test_UserRegistration002(self, setup):

        self.log.info("Testcase test_UserRegistration002 is Started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.rp = RegistrationClass(self.driver)
        self.lp = LoginPageClass(self.driver)

        self.rp.Click_RegistrationPage_Link()
        self.log.info("Click on Registration Page Link")

        self.rp.Enter_Name("Payal")
        self.log.info("Entering Name: Payal")

        email = Generate_Email()
        self.rp.Enter_Email(email)
        self.log.info("Generating Email")
        print(email)

        self.rp.Enter_Password(111213)
        self.log.info("Entering Password 111213")

        self.rp.Enter_ConfirmPassword(111213)
        self.log.info("Confirming Password 111213")

        self.rp.Click_Register_button()
        self.log.info("Click on Register Button")

        if self.lp.Validate_Status() == "Testcase Passed":
            self.log.info("Testcase test_UserRegistration002 is Passed")
            self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")  # (C:\Users\hp\PycharmProjects\Credkart_Pytest\Screenshots)
            assert True
        else:
            self.log.info("Testcase test_UserRegistration002 is Failed")
            self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002.png")
            assert False

        self.log.info("Testcase test_UserRegistration002 is Completed")


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=3))  # random 3 char lower case  e.g. abc
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"  # random 3 char + domain


## pytest -v -s -n=1 --html=HtmlReports/report.html --browser chrome
## pytest -v -s -n=3 --html=HtmlReports/report.html --browser firefox
## pytest -v -s -n=2 --html=HtmlReports/report.html --browser edge



