import pytest
import softest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from ddt import ddt,data,unpack,file_data
#driver = None

from pages.textbox_page import TextBox
from testcases.conftest import driver

#so I just firstly write a test and then refactor it to look good and be optimal

"""
Manual steps:
init page (provide url) 
find element
make input
repeat for each field
click "submit"

#softest.TestCase
"""

@pytest.mark.usefixtures("setup") #I think I don't need fixture to get url because different pages need dif. urls
@ddt
class TestTextBoxPage(softest.TestCase):
    #@pytest.fixture(autouse=True)
    #global driver
    #driver = webdriver.Chrome()
    #driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
    #driver.maximize_window()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tb = TextBox(self.driver)

    #DDT here
    #@data(("Rndomsurname","email@yahoo.com", "21113 Bulevar Oslobozdenija 10 Novi Sad Serbia", "Qwert1234"),("123456","123456", "123456", "123456"))
    #@unpack
    def test_text_boxes_are_filled(self, surname="Alala", email="email@yahoo.com", address="21113 Bulevar Oslobozdenija 10 Novi Sad Serbia", pwd="Qwert1234"):
        filling_result = self.tb.enter_text_boxes(surname, email, address, pwd)
        time.sleep(3)
        print(filling_result)


