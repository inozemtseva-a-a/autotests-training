from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

class TextBox:
    def __init__(self):
        self.driver = webdriver.Chrome #hardcode for now
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")  # I'll change the logic later
        self.driver.maximize_window()

    FULL_NAME_FIELD = "//input[@id='fullname']"
    EMAIL_FIELD = "//input[@id='email']"
    ADDRESS_FIELD = "//textarea[@id='address']"
    PASSWORD_FIELD = "//input[@id='password']"
    SUBMIT_BUTTON = "//input[@value='Submit']"

    def getFullName(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FULL_NAME_FIELD)

    def getEmail(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_FIELD)

    def getAddress(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ADDRESS_FIELD)

    def getPassword(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_FIELD)

    def getSubmitButton(self):
        return self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

    #I can add DDT here from file
    def enterTextBoxes(self):
        self.getFullName().send_keys("Rndomsurname")
        self.getEmail().send_keys("email@yahoo.com")
        self.getAddress().send_keys("21113 Bulevar Oslobozdenija 10 Novi Sad Serbia")
        self.getPassword().send_keys("Qwert1234")
        self.getSubmitButton().click()
