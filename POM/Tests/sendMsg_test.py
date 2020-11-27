import unittest
from selenium import webdriver
import time
from POM.Pages.mainPage import mainPage
from POM.Pages.contactUsPage import ContactUsPage


class SendMsgTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
        cls.driver.maximize_window()
        time.sleep(3)

    def test_sendMassage_test(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        firstsite = mainPage(driver)
        firstsite.goToContactUs()
        time.sleep(5)

        contactsite = ContactUsPage(driver)
        contactsite.enter_text_message("jakis text")
        contactsite.enter_order_reference("1234")
        contactsite.enter_email_address("example13@mail.com")
        time.sleep(4)
        contactsite.click_send()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
