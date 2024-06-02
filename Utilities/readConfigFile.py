import configparser

config = configparser.RawConfigParser()      # This (configparser.RawConfigParser()) method is use to read the common data from config.ini file
                                             # .ini file we have created to save the common data

config.read("C:\\Users\\hp\\PycharmProjects\\Credkart_Pytest\\Configuration\\config.ini")

class Readconfig():

    @staticmethod
    def getUserEmail():
        UserEmail = config.get('login data', 'UserEmail')  # this is going to fetch data from common data section and from Usermail field
        return UserEmail

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'Password')
        return Password

    @staticmethod
    def getFirstName():
        FirstName = config.get('Personal data', 'FirstName')
        return FirstName

    @staticmethod
    def getLastName():
        LastName = config.get('Personal data', 'LastName')
        return LastName

    @staticmethod
    def getPhone():
        Phone = config.get('Personal data', 'Phone')
        return Phone

    @staticmethod
    def getAddress():
        Address = config.get('Personal data', 'Address')
        return Address

    @staticmethod
    def getZipCode():
        ZipCode = config.get('Personal data', 'ZipCode')
        return ZipCode

    @staticmethod
    def getOwnerName():
        OwnerName = config.get('Card data', 'OwnerName')
        return OwnerName

    @staticmethod
    def getCVV():
        CVV = config.get('Card data', 'CVV')
        return CVV

    @staticmethod
    def getCardNumber():
        CardNumber = config.get('Card data', 'CardNumber')
        return CardNumber


















