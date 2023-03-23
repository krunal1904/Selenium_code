# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# import time


# class DockerApp:

#     desired_caps={
#         "deviceName": "samsung Galaxy",
#        "platformName": "Android",
#         "platformVersion": "11.0",
#         "browserName": "chrome",
#         "uid": "emulator-5554"
#     }
    
#     def launch_appium_driver(self):
#         global driver
#         driver=webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
#         time.sleep(5)
#         driver.update_settings({"waitForIdleTimeout": 100})
    
#     def register_validation(self):
#         if  driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/textViewNormalLogin").is_displayed():
#             print(" device..")
#             driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/textViewNormalLogin").click()
#             time.sleep(5)

#     def close_driver(self):
#         driver.quit

# obj=DockerApp()
# obj.launch_appium_driver()
# obj.register_validation()
# obj.close_driver()




from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time





class DockerApp:
    desired_caps = {
                    "deviceName" : "Samsung Galaxy",
                    "platformName" : "Android",
                    "platformVersion" : "11.1",
                    "udid" : "emulator-5554",
                    "app" : "C:/Users/158332/Downloads/naukri-com-17-1.apk"
                    }
    def launch_Appium_Driver(self):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub",self.desired_caps)
        time.sleep(5)
        driver.update_settings({"waitForIdleTimeout": 100})


    def register_validation(self):
        if  driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/textViewNormalLogin").is_displayed():
            print(" device..")
            driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/textViewNormalLogin").click()
            time.sleep(5)

    def logo_validation(self):
        try:
            if driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Get started on Naukri']").is_displayed():
                print("validate")
        
        except:
            print("fail")

    def text_validation(self):
        try:
            if driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[2]").is_displayed():
                print("Get personalised job recommendations based on profile is present")
            if driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[3]").is_displayed():
                print("Track your job applications and get real-time updates is present")
            if driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[4]").is_displayed():
                print("Recruiters directly connect with eligible candidates via chat is present")


        except:
            print("fail")

    def link_validation(self):
        try:
            if driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Already have an account?']").is_displayed():
                print("Already have an account? is present")

            if driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Login']").is_displayed():
                print("Login is available")

        except:
            print("fail")
            

    def close_driver(self):
         driver.quit()

   

   
obj=DockerApp()
obj.launch_Appium_Driver()
# obj.logo_validation()
obj.link_validation()
# obj.register_validation()
# obj.close_driver()