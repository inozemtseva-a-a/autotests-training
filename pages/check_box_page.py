from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

class CheckBox:
    def __init__(self):
        self.driver = webdriver.Chrome  # hardcode for now

    def GetPage(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/check-box.php")
        self.driver.maximize_window()