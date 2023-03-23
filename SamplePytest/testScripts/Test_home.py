import time
import sys

import pytest

from testScripts.conftest import jsonData
# from locators.google_locator import google_logo
sys.path.append("C/Users/158332/PycharmProjects/pythonProject")
from pageObject.SampleHomePage import einfochips_Home
from locatorsHTML.SampleHome import einfochips_logo


@pytest.mark.usefixtures("browser")
class Testeinfochips:           #create class
    #open link
    def test_einfochips_link(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        time.sleep(2)

    # validate logo
    def test_logo(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.logo_validation(einfochips_logo())
        print("logo is present")

    # validate header
    def test_header(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.header_validate()
        print("done")

    #hower and click
    def test_hower_click(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.hower_and_click()
        print("done")

    #test url and title
    def test_url_title(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.hower_and_click()
        obj.url_and_title()
        print("done")

    #click logo
    def test_click_logo(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.hower_and_click()
        obj.logo_click()

    #scroll page
    def test_scroll(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        time.sleep(2)
        obj.scroll_page()

    # validate placeholder
    def test_placeholder(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.scroll_page()
        obj.placeholder_name()
    # click on Contact us and goto new page, fill the form,close the tab
    def test_form(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.scroll_page()
        time.sleep(2)
        obj.contact_us()
        time.sleep(5)

    def test_validate_spec(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.specializaton()

    def test_src(self,jsonData):
        obj = einfochips_Home(self.driver)
        obj.launch_with_url(jsonData["url_einfo"])
        obj.validate_src()











