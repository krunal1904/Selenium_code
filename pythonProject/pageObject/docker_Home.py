from selenium.webdriver.common.by import By
from testData import testdata
import testData.testdata
from locators import docker_locator


class docker_Home:

    def __init__(self, driver):
        self.driver=driver

    def launch_app_with_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def docker_link_print(self):
        print(self.driver.title)
        links = self.driver.find_elements(By.XPATH, docker_locator.all_link())
        print(len(links))
        for i in links:
            print(i.text)

    def docker_header(self):
        menu=(testData.testdata.resdXMLAsPerNode("header").split(","))
        for i in menu:
            if self.driver.find_element(By.XPATH, docker_locator.docker_link(i)).is_displayed():
                print(i)

