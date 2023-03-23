import time
import sys
import pytest
sys.path.append("C/Users/158332/PycharmProjects/pythonProject")
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("appiumdriver")
class TestDockerApp:
    def test_docker_logo(self):

        print("start logo testing using appium")
        self.driver.get("https://www.docker.com")
        docker_logo=self.driver.find_elements(By.XPATH,"//li[@class='logo']")
        assert len(docker_logo) > 0























    # @pytest.mark.regression
    # def test_google_searchbox(self):

    #     obj = Google_Home(self.driver)
    #     obj.launch_app_with_url("https://google.com/")
    #     time.sleep(3)

    # @pytest.mark.smoke
    # def test_google_title(self):

    #     obj = Google_Home(self.driver)
    #     obj.launch_app_with_url("https://google.com/")
    #     obj.validate_google_title("Google")
