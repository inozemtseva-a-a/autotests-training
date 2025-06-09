from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver

class CheckBox(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # hardcode for now

    ELEMENTS_BUTTON = "//button[normalize-space()='Elements']"
    CHECKBOX_BUTTON = "//a[normalize-space()='Check Box']"
    PLUS_MAIN_LEVEL_1_BUTTON = ""
    PLUS_MAIN_LEVEL_2_BUTTON = ""
    MAIN_LEVEL_1_CHECKBOX = "c_bs_1"
    MAIN_LEVEL_2_CHECKBOX = "c_bs_2"
    SUB_LEVEL_1_CHECKBOX = ""
    SUB_LEVEL_2_CHECKBOX = ""
    SUB_LEVEL_3_CHECKBOX = ""
    SUB_LEVEL_4_CHECKBOX = ""
    LAST_LEVEL_1_CHECKBOX = ""
    LAST_LEVEL_2_CHECKBOX = ""
    LAST_LEVEL_3_CHECKBOX = ""
    LAST_LEVEL_4_CHECKBOX = ""
    LAST_LEVEL_5_CHECKBOX = ""
    LAST_LEVEL_6_CHECKBOX = ""
    LAST_LEVEL_7_CHECKBOX = ""
    LAST_LEVEL_8_CHECKBOX = ""
    LAST_LEVEL_9_CHECKBOX = ""
    LAST_LEVEL_10_CHECKBOX = ""
    LAST_LEVEL_11_CHECKBOX = ""
    LAST_LEVEL_12_CHECKBOX = ""
    LAST_LEVEL_13_CHECKBOX = ""
    LAST_LEVEL_14_CHECKBOX = ""
    LAST_LEVEL_15_CHECKBOX = ""
    LAST_LEVEL_16_CHECKBOX = ""


    def get_page(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ELEMENTS_BUTTON)

    def get_checkboxes(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHECKBOX_BUTTON)
    #
    # def get_plus_main_level_1(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.PLUS_MAIN_LEVEL_1_BUTTON)
    #
    # def get_plus_main_level_2(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.PLUS_MAIN_LEVEL_2_BUTTON)

    def get_checkbox_main_level_1(self):
        return self.wait_until_element_is_clickable(By.ID, self.MAIN_LEVEL_1_CHECKBOX)

    def get_checkbox_main_level_2(self):
        return self.wait_until_element_is_clickable(By.ID, self.MAIN_LEVEL_2_CHECKBOX)

    # def get_plus_sub_level_1(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.SUB_LEVEL_1_CHECKBOX)
    #
    # def get_plus_sub_level_2(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.SUB_LEVEL_2_CHECKBOX)
    #
    # def get_plus_sub_level_3(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.SUB_LEVEL_3_CHECKBOX)
    #
    # def get_plus_sub_level_4(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.SUB_LEVEL_4_CHECKBOX)
    #
    # def get_plus_last_level_1(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_1_CHECKBOX)
    #
    # def get_plus_last_level_2(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_2_CHECKBOX)
    #
    # def get_plus_last_level_3(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_3_CHECKBOX)
    #
    # def get_plus_last_level_4(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_4_CHECKBOX)
    #
    # def get_plus_last_level_5(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_5_CHECKBOX)
    #
    # def get_plus_last_level_6(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_6_CHECKBOX)
    #
    # def get_plus_last_level_7(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_7_CHECKBOX)
    #
    # def get_plus_last_level_8(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_8_CHECKBOX)
    #
    # def get_plus_last_level_9(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_9_CHECKBOX)
    #
    # def get_plus_last_level_10(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_10_CHECKBOX)
    #
    # def get_plus_last_level_11(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_11_CHECKBOX)
    #
    # def get_plus_last_level_12(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_12_CHECKBOX)
    #
    # def get_plus_last_level_13(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_13_CHECKBOX)
    #
    # def get_plus_last_level_14(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_14_CHECKBOX)
    #
    # def get_plus_last_level_15(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_15_CHECKBOX)
    #
    # def get_plus_last_level_16(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.LAST_LEVEL_16_CHECKBOX)

    #getting page
    def opening_page(self):
        #self.get_page().click()
        self.get_checkboxes().click()


    def selecting_checkboxes_main_1(self):
        self.get_checkbox_main_level_1().click()
        m1_selected = self.get_checkbox_main_level_1().is_selected()
        return "It should be selected" + m1_selected

    def selecting_checkboxes_main_2(self):
        m2_not_selected = self.get_checkbox_main_level_2().is_selected()
        return "It shouldn't be selected" + m2_not_selected


