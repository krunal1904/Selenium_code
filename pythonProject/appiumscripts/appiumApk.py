from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


class DockerApp:

    desired_caps={
        "deviceName": "samsung Galaxy",
        "platformName": "Android",
        "platformVersion": "11.0",
        "uid": "emulator-5554",
        "deviceNAme":"device 1",
        "app":"C:/Users/158332/Downloads/naukri-com-17-1.apk"
    }
    
    def launch_appium_driver(self):
        global driver
        driver=webdriver.Remote("C:/Users/158332/Downloads/naukri-com-17-1.apk", self.desired_caps)

        time.sleep(2)

    def docker_logo_validation(self):

        try:

            docker_logo = self.driver.find_elememt(AppiumBy.XPATH, "//li[@class='logo']")
            if docker_logo.is_displayed():
                print("Docker logo is present")
        
        except:

            print("not present")

    def close_driver(self):
        driver.quit

obj=DockerApp()
obj.launch_appium_driver()
obj.docker_logo_validation()
obj.close_driver()