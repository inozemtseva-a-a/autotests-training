from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver


class TextBox(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        return self.wait_until_element_is_clickable(By.XPATH, self.ADDRESS_FIELD)

    def get_password(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_FIELD)

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

    def enter_text_boxes(self, surname, email, address, pwd):
        self.get_full_name().send_keys(surname)
        self.get_email().send_keys(email)
        self.get_address().send_keys(address)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()
        #return "End"

    # def checking_emptiness(self):
    #     values_fullname = self.get_full_name().get_attribute("value")
    #     if values_fullname == "":
    #         print("empty")
    #     else:
    #         print("Not empty!")

        # self.get_email().
        # self.get_address().
        # self.get_password().
