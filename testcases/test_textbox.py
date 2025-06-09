import pytest
import softest
import time
from ddt import ddt,data,unpack,file_data
from pages.textbox_page import TextBox
from utilities.utility import Utils


#so I just firstly write a test and then refactor it to look good and be optimal
#need to redo the logic because this test doesn't test anything

@pytest.mark.usefixtures("setup") #I think I don't need fixture to get url because different pages need dif. urls
@ddt
class TestTextBoxPage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tb = TextBox(self.driver)

    #DDT here (The simplest variant for now)
    #@data(("Rndomsurname","email@yahoo.com", "21113 Bulevar Oslobozdenija 10 Novi Sad Serbia", "Qwert1234"),("123456","123456", "123456", "123456"))
    @data(*Utils.read_data_from_csv("C:\\python-selenium\\AutotestsTrening\\testdata\\testdata.csv"))
    @unpack
    def test_text_boxes_are_filled(self, surname, email, address, pwd):
        filling_result = self.tb.enter_text_boxes(surname, email, address, pwd)
        time.sleep(3)  #hardcoded for now
        print(filling_result)
        # output_checking = self.checking_emptiness()
        # print(output_checking)



