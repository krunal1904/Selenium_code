import json
import time
import sys

import pytest

sys.path.append("C/Users/158332/PycharmProjects/pythonProject")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from appium import webdriver



@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.instance.driver=driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver=driver
    driver.maximize_window()

    yield driver

    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser")

@pytest.fixture()
def params(request):
    params ={}
    params['browser']=request.config.getoption('--browser')
    return params


@pytest.fixture()
def multiple_browser(request, params):
    web_driver=""
    if params["browser"]=='chrome':
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if params["browser"]=='firefox':
       web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.instance.driver =web_driver
    web_driver.maximize_window()

    yield webdriver
    web_driver.close()

@pytest.fixture()
def jsonData():
    with open('C:/Users/158332/PycharmProjects/pythonProject/testData/testdata.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def appiumdriver(request):
    print("initiating chrome driver")

    capabilities={

        "deviceName": "samsung Galaxy",
       "platformName": "Android",
        "platformVersion": "11.1",
        "browserName": "chrome",
        "uid": "emulator-5554"
    }
    
    driver=webdriver.Remote("https://localhost:4723", capabilities)
    request.instance.driver=driver
    driver.maximize_window()

    yield driver

    driver.close()