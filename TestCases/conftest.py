import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://automation.credence.in")
#     return driver

# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.get("https://automation.credence.in")
#     return driver


# @pytest.fixture
# def setup():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get("https://automation.credence.in/login")
#     return driver


# @pytest.fixture
# def setup():
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.get("https://automation.credence.in/login")
#     return driver


# RUNNING PYTEST WITH REQUIRED BROWSER WITH COMMAND #

def pytest_addoption(parser):
    parser.addoption("--browser")  # Now --driver is recognized to your pytest/python


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")  # --browser(agr) will get value for browser e.g chrome, edge

    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'edge':
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    yield driver
    driver.quit()
