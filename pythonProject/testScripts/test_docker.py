import time
import sys


import pytest
from locators.docker_locator import docker_link
sys.path.append("C/Users/158332/PycharmProjects/pythonProject")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.docker_Home import docker_Home

# @pytest.mark.usefixtures("multiple_browser")
class TestdockerApp:
    # @pytest.mark.smoke
    # def test_docker_link(self, browser):
    #     obj = docker_Home(browser)
    #     obj.launch_app_with_url("https://docker.com/")
    #     # obj.docker_link_print()
    #     obj.docker_header()

    def test_docker_logo(self,jsonData):

        obj=docker_Home(self.driver)
        obj.launch_app_with_url(jsonData['url_docker'])
        obj.docker_link_print()



