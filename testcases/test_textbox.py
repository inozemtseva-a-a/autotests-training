import pytest
import softest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

#@pytest.mark.usefixtures("setup")
class TestTextBoxPage():
    def text_box_imput(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php") #I'll change the logic later
        driver.maximize_window()
        time.sleep(3) #it'll be removed also and I'll add waits
        fullname = driver.find_element(By.XPATH, "//input[@id='fullname']")
        fullname.send_keys("Rndomsurname")
        time.sleep(1)

        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.send_keys("email@yahoo.com")
        time.sleep(1)

        address = driver.find_element(By.XPATH, "//textarea[@id='address']")
        address.send_keys("21113 Bulevar Oslobozdenija 10 Novi Sad Serbia")
        time.sleep(1)

        address = driver.find_element(By.XPATH, "//input[@id='password']")
        address.send_keys("Qwert1234")
        time.sleep(1)

        submitbutton = driver.find_element(By.XPATH, "//input[@value='Submit']")
        submitbutton.click()
        time.sleep(3)

testing = TestTextBoxPage()
testing.text_box_imput()