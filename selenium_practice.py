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
from selenium.webdriver.chrome.options import Options
import support

class test:
    def launch(self):
        global driver
        # options=Options()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    #options=options
        driver.maximize_window()

    def screenshot(self):
        try:

            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(2)

            if driver.find_element(By.XPATH,"(//a[@class='navbar-brand img-flui'])[1]").is_displayed():
                print("present")

            time.sleep(2)

        except:
            driver.save_screenshot("C:/Users/158332/PycharmProjects/p1/screenshot/logo.png")
            driver.close()
            print("logo is present")

    def autodropdown(self):
            try:

                driver.get("https://www.pizzahut.co.in/")
                driver.implicitly_wait(10)

                if driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").is_displayed():
                    print("present")
                    time.sleep(5)
                    driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").send_keys("chandlodiya")
                    if driver.find_element(By.XPATH,"//input[@placeholder='Enter your location for delivery']").is_selected():
                        driver.find_element(By.XPATH,"//input[@placeholder='Enter your location for delivery']").click()
                        time.sleep(5)


                    print("done")


            except:
                print("error")


    def scroll_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)

            if driver.find_element(By.XPATH,"//a[@href='/docs/concepts/workloads/controllers/job/']").is_displayed():
                driver.find_element(By.XPATH,"//a[@href='/docs/concepts/workloads/controllers/job/']").location_once_scrolled_into_view
                time.sleep(2)
                driver.find_element(By.XPATH,"//a[@href='/docs/concepts/workloads/controllers/job/']").click()
                time.sleep(3)
            time.sleep(2)

        except:
            print("error")

    def right_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)

            logo=driver.find_element(By.XPATH,"(//a[@class='navbar-brand img-fluid'])[1]")

            if logo.is_displayed():
                actionChains=ActionChains(driver)
                actionChains.context_click(logo).perform()
                time.sleep(3)


        except:
            print("error")

    def double_click(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(2)

            logo = driver.find_element(By.XPATH, "(//a[@class='navbar-brand img-fluid'])[1]")
            if logo.is_displayed():
                actionChains = ActionChains(driver)
                actionChains.double_click(logo).perform()
                print("double click is working")
                time.sleep(3)
        except:
            print("double click isn't working")
            driver.quit()


    def close_app(self):
        driver.quit()

    def header_check(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(2)
            menu = (common.resdXMLAsPerNode("headermenu")).split(",")
            # print(menu)
            for i in menu:
                try:
                    if driver.find_element(By.XPATH,"(//a[text()='"+i+"'])[1]").is_displayed():
                        print("header menu is available==>"+i)

                except:
                    print("not working")

        except:
            print("error")

    def header_check2(self):
        try:
            driver.get("https://www.docker.com/")
            driver.implicitly_wait(2)
            menu = (common.resdXMLAsPerNode("headermenu2")).split(",")
            # print(menu)
            for i in menu:
                try:
                    if driver.find_element(By.XPATH, "(//a[text()='" + i + "'])[1]").is_displayed():
                        print("header menu is available==>" + i)

                except:
                    print("not working")

        except:
            print("error")

    def upload(self):
        try:

            driver.get("https://the-internet.herokuapp.com/upload")
            driver.implicitly_wait(10)

            if driver.find_element(By.XPATH,"//input[@id='file-upload']").is_displayed():
                driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:/Users/158332/PycharmProjects/p1/screenshot/logo.png")
                driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
                print("ok")
            if driver.find_element(By.XPATH,"//div[@id='uploaded-files']").is_displayed():
                print("validate")


            time.sleep(2)

        except:
            print("error")

    def english(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(2)

            if driver.find_element(By.XPATH,"(//a[@class='nav-link dropdown-toggle'])[2]").is_displayed():
                driver.find_element(By.XPATH,"(//a[@class='nav-link dropdown-toggle'])[2]").click()
                lst=driver.find_elements(By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']")
                for i in lst:
                    print(i.text)


        except:
            print("error")

    def read_book(self):
        try:
            driver.get("https://testautomationpractice.blogspot.com/")
            driver.implicitly_wait(2)
            print(support.read_book_html(driver,"Learn Selenium","Price"))


        except:
            print("error")


    def auto_Select_Drop_Down(self):
        try:

            driver.get("https://www.pizzahut.co.in/")
            driver.implicitly_wait(3)

           # Type Address in Address Search Box ...
            time.sleep(2)
            try:
                if driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                    driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").click()
            except:
                print("Preselect option is not available....")


            if driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").is_displayed():
                print("Kubernetes Logo is present ....")
                driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").send_keys("Lulu mall bangalore")
                time.sleep(2)
                if driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").is_displayed():
                    driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").click()

                    if driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                        print("User successfully selected the Auto Select drop down option....")
            time.sleep(3)
        except:
            print("fail")


    def href_link(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)

            links=driver.find_elements(By.TAG_NAME,"a")
            for i in links:
                print(i.get_attribute('href'))

        except:
            print("eroors")


    def css_selector(self):
        try:
            driver.get("https://kubernetes.io/")
            driver.implicitly_wait(10)

            links=driver.find_elements(By.CSS_SELECTOR, 'button#hamburger')
            print(links)

        except:
            print("eroors")



c=test()
c.launch()
# c.screenshot()
# c.autodropdown()
c.auto_Select_Drop_Down()
c.close_app()