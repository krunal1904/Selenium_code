from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class NaukriApp:
    desired_caps = {
                    "deviceName" : "Samsung Galaxy",
                    "platformName" : "Android",
                    "platformVersion" : "11.1",
                    "udid" : "emulator-5554",
                    "app" : "C:/Users/158332/Downloads/naukri-com-17-1.apk"
                    }
    def launch_Appium_Driver(self):
        global driver
        driver = webdriver.Remote("http://localhost:4725/wd/hub",self.desired_caps)
        time.sleep(5)
        driver.update_settings({"waitForIdleTimeout": 100})


    def tap_button(self):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(770, 583)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def scroll_check(self):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(774, 505)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(713, 1966)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(679, 844)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        # driver.swipe(470, 800, 470, 50, 400)

    def view_all(self):
        try:
            el1 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/tv_view_all")
            el1.click()
            time.sleep(3)

            #counting company and print names
            total=driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/tv_company_name']")
            rating=driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/tv_rating']")
            print(len(total))
            print(len(rating))
            for k in total:
                comp_name = k.get_attribute('text')
                print("Company name is:-->", comp_name)

            for m in rating:
                rating = m.get_attribute('text')
                print("Rating ", rating)


        except:
         print("not working")

    def search_job(self):
        el2 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/editTextSearch")
        el2.click()
        time.sleep(3)

        el2 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/et_skills")
        el2.click()
        el2.send_keys("Automation")
        time.sleep(2)

        el5 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/et_loc")
        el5.click()
        el5.send_keys("Ahmedabad")
        time.sleep(2)

        el3 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/b_search")
        el3.click()
        time.sleep(2)

        el8 = driver.find_element(by=AppiumBy.ID, value="naukriApp.appModules.login:id/imageViewFilter")
        el8.click()
        time.sleep(2)

        filter = driver.find_elements(AppiumBy.XPATH,"//android.widget.CheckBox[@resource-id='naukriApp.appModules.login:id/checkBoxMultipleSelect']")
        print(len(filter))
        for k in filter:
            filter_name = k.get_attribute('text')
            print("Filter option:-->", filter_name)
        # fname = driver.find_element(AppiumBy., "//android.widget.CheckBox[@text='hybrid']")
        # # f_name=fname.getattribute('text')
        # print(fname)

            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(518, 814)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)











    def close_app(self):
        driver.quit()




obj=NaukriApp()
obj.launch_Appium_Driver()
# obj.scroll_check()
# obj.view_all()
obj.tap_button()
obj.search_job()
obj.close_app()