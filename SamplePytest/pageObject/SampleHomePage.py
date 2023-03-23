import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from reusable import Reusable
from locatorsHTML.SampleHome import Eic_header
from selenium.webdriver.common.action_chains import ActionChains
from locatorsHTML.SampleHome import Eic_hower
from locatorsHTML.SampleHome import Eic_click
from locatorsHTML.SampleHome import Eic_link
from locatorsHTML.SampleHome import Eic_title
from locatorsHTML.SampleHome import einfochips_logo
from locatorsHTML.SampleHome import Eic_scroll
from locatorsHTML.SampleHome import Eic_plc
from locatorsHTML.SampleHome import Eic_plc_name
from locatorsHTML.SampleHome import Eic_form
from locatorsHTML.SampleHome import form_data
from locatorsHTML.SampleHome import Eic_dropdown
from locatorsHTML.SampleHome import Eic_spec
from locatorsHTML.SampleHome import Eic_check_src



class einfochips_Home:

    def __init__(self, driver):
        self.driver=driver
    # launch url
    def launch_with_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # logo validation
    def logo_validation(self, logo):
        print(self.driver.title)
        logo = self.driver.find_elements(By.XPATH, logo)
        assert len(logo) > 0
    # header validation

    def header_validate(self):
            try:
                menu = (Reusable.resdXMLAsPerNode("headermenu")).split(",")
                # print(menu)
                for i in menu:
                    try:
                        if self.driver.find_element(By.XPATH,Eic_header(i)).is_displayed():
                            print("header menu is available==>" + i)

                    except:
                        print("not working")

            except:
                print("error")

    #hower and click
    def hower_and_click(self):
        try:
            a = ActionChains(self.driver)
            m = self.driver.find_element(By.XPATH,Eic_hower())
            a.move_to_element(m).perform()
            self.driver.find_element(By.XPATH, Eic_click()).click()


        except:
            print("not hower")

    #match url and title
    def url_and_title(self):
        try:
            get_url = self.driver.current_url
            url=str(get_url)
            print(url)
            get_title=self.driver.title
            print(get_title)
            if url == Eic_link():
                print("link validate")
            else:
                print(("not link valid"))

            if get_title == Eic_title():
                print("title validate")
            else:
                print(("not title valid"))


        except:
            print("no url")

    # click on logo
    def logo_click(self):
        try:
            k=self.driver.find_element(By.XPATH, einfochips_logo)
            k.click()
            print("clicked")


        except:
            print("click")

    # scroll the web page
    def scroll_page(self):
        try:
            self.driver.find_element(By.XPATH, Eic_scroll('a')).location_once_scrolled_into_view
            print("scroll")
            time.sleep(2)

        except:
            print("not scroll")

    # validate place holder
    def placeholder_name(self):
         try:
             name = self.driver.find_element(By.XPATH, Eic_plc())
             p=name.get_attribute('placeholder')
             print(p)
             if p == Eic_plc_name():
                 print("match")

         except:
            print("not valid text")

    # form fill by clicking on contact us
    def contact_us(self):
        try:
            self.driver.find_element(By.XPATH, Eic_form('c')).click()
            print("clicked")

            p = self.driver.current_window_handle
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
            self.driver.switch_to.window(chld)

            time.sleep(2)

            self.driver.find_element(By.XPATH, Eic_scroll('k')).location_once_scrolled_into_view
            time.sleep(2)

            b=self.driver.find_element(By.XPATH, Eic_form('n'))
            b.click()
            b.send_keys(form_data('name'))
            time.sleep(2)
            b = self.driver.find_element(By.XPATH, Eic_form('e'))
            b.click()
            b.send_keys(form_data('email'))
            time.sleep(2)
            b = self.driver.find_element(By.XPATH, Eic_form('num'))
            b.click()
            b.send_keys(form_data('number'))
            time.sleep(2)
            b = self.driver.find_element(By.XPATH, Eic_form('com'))
            b.click()
            b.send_keys(form_data('company'))
            time.sleep(2)

            drp = self.driver.find_element(By.XPATH, Eic_dropdown())
            d = Select(drp)
            time.sleep(2)
            d.select_by_index(2)

            b = self.driver.find_element(By.XPATH, Eic_form('comm'))
            b.click()
            b.send_keys(form_data('comments'))
            time.sleep(2)

            self.driver.close()

        except:
            print("not filled")

    def specializaton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Eic_scroll('p')).location_once_scrolled_into_view
        time.sleep(2)
        try:
            if self.driver.find_element(By.XPATH, Eic_scroll('p')).is_displayed():
                print("Championing Innovation Driven Business is present")
                count = []
                for j in range(5, 15):
                    spec = self.driver.find_element(By.XPATH, Eic_spec(j))
                    count.append(spec)
                print(len(count))
        except:
             print("not present")

    def validate_src(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Eic_scroll('p')).location_once_scrolled_into_view
        time.sleep(2)
        try:
            if self.driver.find_element(By.XPATH, Eic_check_src('a')).is_displayed():
                print("Aerospace is present")
                src = self.driver.find_element(By.XPATH, Eic_check_src('b'))
                final_src = src.get_attribute("src")
                print(final_src)




        except:
            print("not working")



