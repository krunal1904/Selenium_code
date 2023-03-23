import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from reusable import common
import self as self
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class test:
    def launch(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

    def test_case(self):
        try:
            driver.get("https://the-internet.herokuapp.com/checkboxes")
            driver.implicitly_wait(10)

            if not driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[1]").is_selected():
                 print("pass")
                 driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[1]").click()
                 time.sleep(5)
            else:
                 print("fail")

            if driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[2]").is_selected():
                 print("pass")
                 driver.find_element(By.XPATH, "(//form[@id='checkboxes']/input)[2]").click()
                 time.sleep(2)
            else:
                print("fail")

        except:
            print("error")

    def test_case2(self):
        try:
            driver.get("https://www.webucator.com/account/login/")
            driver.implicitly_wait(10)


            driver.find_element(By.XPATH,"//input[@name='login']").clear()
            driver.find_element(By.XPATH, "//input[@name='login']").send_keys("test@test.com")
            driver.find_element(By.XPATH, "//input[@name='password']").clear()
            driver.find_element(By.XPATH, "//input[@name='password']").send_keys("password")
            driver.find_element(By.XPATH, "//button[@class='form-control btn btn-secondary f-18 h-40 mt-20']").click()
            time.sleep(5)

            print(driver.find_element(By.XPATH,"//strong").text)
            if driver.find_element(By.XPATH, "//strong").text==common.resdXMLAsPerNode("error"):
                print("error:--The e-mail address and/or password you specified are not correct.")
            else:
                print("fail")

        except:
            print("error")

    def test_case3(self):
        try:
            driver.get("https://www.webucator.com/account/password/reset/")
            driver.implicitly_wait(10)

            driver.find_element(By.XPATH, "//input[@name='email']").clear()
            driver.find_element(By.XPATH, "//input[@name='email']").send_keys(" ")
            driver.find_element(By.XPATH, "//button[@class='form-control btn btn-secondary f-18 h-40 mt-20 mb-50']").click()
            time.sleep(5)

        except:
            print("error")

    def test_case4(self):
        try:
            driver.get("https://www.webucator.com/")
            driver.implicitly_wait(10)

            lst=list(driver.find_elements(By.XPATH,"//h4[text()='About Us']/../ul/li/a"))
            print(len(lst))
            time.sleep(6)

        except:
            print("error")

    def test_case5(self):
        try:
            driver.get("https://the-internet.herokuapp.com/dropdown")
            driver.implicitly_wait(10)

            select=Select(driver.find_element(By.ID,'dropdown'))

            select.select_by_index(2)

            time.sleep(2)

            select.select_by_visible_text('Option 2')

            time.sleep(3)

            select.selection_by_value('2')
            time.sleep(2)



        except:
            print("error")

    def test_case6(self):
        try:
            driver.get("https://www.docker.com/")
            driver.implicitly_wait(10)

            ele = driver.find_element(By.XPATH,"//a[text()='Developers'][1]")

            ActionChains(driver).move_to_element(ele).perform()
            time.sleep(3)
            driver.find_element(By.XPATH, "(//a[text()='Community'])").click()
            driver.implicitly_wait(3)

            if "community" in driver.current_url:
                print("pass")
            else:
                print("fail")

        except:
            print("error")

    def test_case7(self):
        try:
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            driver.implicitly_wait(10)

            driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
            alert=Alert(driver)
            if alert.text == 'I am a JS Alert':
                alert.accept()
                time.sleep(1)
                driver.find_element(By.XPATH,"//p[text()='You successfully clicked an alert']").is_displayed()
                print("pass")
            else:
                print("fail")
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
            time.sleep(1)
            alert=Alert(driver)
            if alert.text == 'I am a JS Confirm':
                alert.dismiss()
                time.sleep(1)
                driver.find_element(By.XPATH, "//p[text()='You clicked: Cancel']").is_displayed()
                print("pass")
            else:
                print("fail")
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
            time.sleep(1)
            alert = Alert(driver)
            if alert.text == 'I am a JS prompt':
                alert.send_keys("krunal")
                alert.accept()
                time.sleep(1)
                driver.find_element(By.XPATH, "//p[text()='You entered: krunal']").is_displayed()
                print("pass")
            else:
                print("fail")

        except:
            print("error")

    def test_case8(self):
        try:

            driver.get("https://docker.com")
            driver.implicitly_wait(10)

            # Click on Twitter Logo ...
            driver.find_element(By.XPATH, "//img[@alt='twitter logo']").click()
            time.sleep(5)
            # Get the Count of Window ....
            windows = driver.window_handles
            size = len(windows)
            parent_window = driver.current_window_handle

            for x in range(size):
                if windows[x] != parent_window:
                    driver.switch_to.window(windows[x])
                    print(driver.title)
                    driver.close()
                    time.sleep(3)
                    break
            # Moving bacck to parent window
            driver.switch_to.window(parent_window)
            print(driver.title)
        except:
            print("Something went wrong")



k=test()
k.launch()
k.test_case8()
# k.test_case2()
# k.test_case3()
# k.test_case4()
# k.test_case5()
# k.test_case6()

