import pytest
import softest
import time
from ddt import ddt,data,unpack,file_data
from utilities.utility import Utils
from pages.check_box_page import CheckBox

@pytest.mark.usefixtures("setup")
class TestCheckBoxPage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.chb = CheckBox(self.driver)

    #test: when checking main 1 is doesn't check main 2
    def test_checkboxes(self):
        resulting = self.chb.get_checkbox_main_level_1()
        resulting2 = self.chb.selecting_checkboxes_main_2()
        time.sleep(3)  #hardcoded for now
        print(resulting)
        print(resulting2)




