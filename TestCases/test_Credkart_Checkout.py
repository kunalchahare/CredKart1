from PageObjects.CheckoutPage import CheckoutPageClass
from PageObjects.LoginPage import LoginPageClass
from Utilities.readConfigFile import Readconfig
from Utilities.Logger import LogGenerator


class Test_CredkartCheckout:
    UserEmail = Readconfig.getUserEmail()
    Password = Readconfig.getPassword()
    FirstName = Readconfig.getFirstName()
    LastName = Readconfig.getLastName()
    Phone = Readconfig.getPhone()
    Address = Readconfig.getAddress()
    ZipCode = Readconfig.getZipCode()
    OwnerName = Readconfig.getOwnerName()
    CVV = Readconfig.getCVV()
    CardNumber = Readconfig.getCardNumber()

    log = LogGenerator.loggen()

    def test_CredkartCheckout01(self, setup):
        self.log.info("Testcase test_CredkartCheckout01 is started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = LoginPageClass(self.driver)
        self.cp = CheckoutPageClass(self.driver)

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

        self.log.info("Click on Product to Buy")
        self.cp.Click_AppleMacbookPro()

        self.log.info("Product Adding to cart")
        self.cp.Click_AddtoCart_Button()

        self.log.info("Proceed To Checkout Page")
        self.cp.Click_ProceedtoCheckout_Button()

        self.cp.Enter_FirstName(self.FirstName)
        self.log.info(("Enter FirstName:" + self.FirstName))
        print("FirstName:", self.FirstName)

        self.cp.Enter_LastName(self.LastName)
        self.log.info(("Enter LastName:" + self.LastName))
        print("LastName:", self.LastName)

        self.cp.Enter_Phone(self.Phone)
        self.log.info(("Enter Phone:" + self.Phone))
        print("Phone:", self.Phone)

        self.cp.Enter_Address(self.Address)
        self.log.info(("Enter Address:" + self.Address))
        print("Address:", self.Address)

        self.cp.Enter_ZipCode(self.ZipCode)
        self.log.info(("Enter ZipCode:" + self.ZipCode))
        print("ZipCode:", self.ZipCode)

        self.cp.Select_State()

        self.cp.Enter_OwnerName(self.OwnerName)
        self.log.info(("Enter OwnerName:" + self.OwnerName))
        print("OwnerName:", self.OwnerName)

        self.cp.Enter_CVV(self.CVV)
        self.log.info(("Enter CVV:" + self.CVV))
        print("CVV:", self.CVV)

        self.cp.Enter_CardNumber(self.CardNumber)
        self.log.info(("Enter CardNumber:" + self.CardNumber))
        print("CardNumber:", self.CardNumber)

        self.cp.Select_ExpirationYear()

        self.cp.Select_ExpirationMonth()

        self.log.info("Click on Continue to Checkout")
        self.cp.Click_Continuetocheckout()

        if self.cp.Validate_Status() == "Testcase Passed":
            self.log.info("Testcase test_CredkartCheckout01 is Passed")
            self.driver.save_screenshot("..\\Screenshot\\test_CredkartCheckout01_Pass.png")
            assert True
        else:
            self.log.info("Testcase test_CredkartCheckout01 is Failed")
            self.driver.save_screenshot("..\\Screenshot\\test_CredkartCheckout01_Fail.png")
            assert False

        self.log.info("Testcase test_CredkartCheckout01 is Completed")





























