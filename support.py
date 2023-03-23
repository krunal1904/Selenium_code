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


def read_book_html(driver,BookName,whatToRead):
    value = "null"
    if whatToRead == "Author":
        value=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr/td[text()='"+BookName+"']/../td[2]").text
    if whatToRead == "Subject":
        value = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr/td[text()='" + BookName + "']/../td[3]").text
    if whatToRead == "Price":
        value = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr/td[text()='" + BookName + "']/../td[4]").text
    return value

