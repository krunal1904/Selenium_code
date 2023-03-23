from datetime import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test:
    def launch(self):
        global driver
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome()
        driver.maximize_window()


    def write_content(self):
        try:

            driver.get("https://the-internet.herokuapp.com/iframe")
            driver.implicitly_wait(10)

            if driver.find_element(By.TAG_NAME, "/p").is_displayed():
                driver.find_element(By.TAG_NAME,"p").click()
                driver.find_element(By.TAG_NAME, "p").clear()
                time.sleep(3)
                driver.find_element(By.TAG_NAME,"p").send_keys("hello kb!")

            time.sleep(2)

        except:
            print("error")

k=Test()
k.launch()
k.write_content()
