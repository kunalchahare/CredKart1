import logging  # built in Python


class LogGenerator:
    @staticmethod
    def loggen():
        # given path and file name
        logfile = logging.FileHandler("C:\\Users\\hp\\PycharmProjects\\Credkart_Pytest\\Logs\\CredKartAutomation.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger = logging.getLogger()
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

# Debug
# info
# Warning
# Error
# Critical
