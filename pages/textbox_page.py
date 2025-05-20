from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver


class TextBox(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #driver = webdriver.Chrome() #hardcode for now
        #driver.get(url)  # I'll change the logic later
        #driver.maximize_window()

#url = "https://www.tutorialspoint.com/selenium/practice/text-box.php"

    FULL_NAME_FIELD = "//input[@id='fullname']"
    EMAIL_FIELD = "//input[@id='email']"
    ADDRESS_FIELD = "//textarea[@id='address']"
    PASSWORD_FIELD = "//input[@id='password']"
    SUBMIT_BUTTON = "//input[@value='Submit']"

    def get_full_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FULL_NAME_FIELD)

    def get_email(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_FIELD)

    def get_address(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ADDRESS_FIELD)

    def get_password(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_FIELD)

    # def get_submit_button(self):
    #     return self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

    #I can add DDT here from file. And it should be in test, not in the page
    def enter_text_boxes(self, surname, email, address, pwd):
        self.get_full_name().send_keys(surname)
        self.get_email().send_keys(email)
        self.get_address().send_keys(address)
        self.get_password().send_keys(pwd)
        self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON).click()
        return "End"
