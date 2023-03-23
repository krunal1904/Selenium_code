import time
from reusable import common
import self as self
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class testselenium:

    def launch_app(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(2)
        driver.get(common.resdXMLAsPerNode("URL"))
        driver.maximize_window()
        time.sleep(2)

        runTitle=driver.title

        if runTitle==common.resdXMLAsPerNode("title"):
            print("true")
        else:
            print("false")

    def testcase_validate(self):
         print(driver.title)
         print(driver.current_url)

    def close_app(self):
        driver.quit()
        return self

k = testselenium()
k.launch_app()
k.testcase_validate()
k.close_app()
#

#
# import time
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as Service
# from selenium.webdriver.common.by import By
#
#
# class Test:
#
#     def LaunchApp(self):
#         global driver
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.implicitly_wait(5)
#         driver.get("https://www.einfochips.com/")
#         driver.maximize_window()
#         time.sleep(5)
#         return self
#
#     def TestCase(self):
#         print(driver.title)
#         print(driver.current_url)
#         if driver.find_element(By.XPATH,
#                                "//a[@title='eInfochips']//img[@class='mk-desktop-logo dark-logo']").is_displayed():
#             print("Pass")
#         else:
#             print("Fail")
#         return self
#
#     def CloseApp(self):
#         driver.quit()
#         return self
#
# test = Test()
# test.LaunchApp()
# test.TestCase()
# test.CloseApp()





