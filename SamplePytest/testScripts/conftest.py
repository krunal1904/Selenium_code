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


@pytest.fixture(scope='class')
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver=driver
    driver.maximize_window()

    yield driver

    driver.close()

@pytest.fixture()
def jsonData():
    with open('C:/Users/158332/PycharmProjects/SamplePytest/testData/testData.json') as config_file:
        data = json.load(config_file)
    return data