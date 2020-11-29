import time
import unittest

from selenium import webdriver

from POM.Pages.contactUsPage import ContactUsPage
from POM.Pages.mainPage import mainPage


class SendMsgTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
        cls.driver.maximize_window()
        time.sleep(3)

    def test_sendMessage_test_valid_data(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        firstsite = mainPage(driver)
        firstsite.goToContactUs()
        time.sleep(5)

        contactsite = ContactUsPage(driver)
        contactsite.set_subject_heading_as_customer_service()
        contactsite.enter_text_message("jakis text")
        contactsite.enter_order_reference("1234")
        contactsite.enter_email_address("example13@mail.com")
        time.sleep(4)
        contactsite.click_send()
        time.sleep(2)
        msg_status = contactsite.check_returned_message_about_message_status_valid_data()
        self.assertEqual(msg_status, "Your message has been successfully sent to our team.")

    def test_sendMessage_invalid_email_test(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        firstsite = mainPage(driver)
        firstsite.goToContactUs()
        time.sleep(1)

        contactsite = ContactUsPage(driver)
        contactsite.enter_text_message("jakis text")
        contactsite.enter_order_reference("1234")
        contactsite.enter_email_address("example13mail.com")
        contactsite.set_subject_heading_as_customer_service()
        contactsite.click_send()
        time.sleep(1)
        msg_status = contactsite.check_returned_message_about_message_status_invalid_data()
        self.assertEqual(msg_status, "Invalid email address.")

    def test_sendMessage_unchoosen_subject_heading_test(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        firstsite = mainPage(driver)
        firstsite.goToContactUs()
        time.sleep(1)

        contactsite = ContactUsPage(driver)
        contactsite.enter_text_message("jakis text")
        contactsite.enter_order_reference("1234")
        contactsite.enter_email_address("example13@mail.com")
        contactsite.click_send()
        time.sleep(1)
        msg_status = contactsite.check_returned_message_about_message_status_invalid_data()
        self.assertEqual(msg_status, "Please select a subject from the list provided.")

    def test_sendMessage_empty_message(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        firstsite = mainPage(driver)
        firstsite.goToContactUs()
        time.sleep(1)

        contactsite = ContactUsPage(driver)
        contactsite.set_subject_heading_as_customer_service()
        contactsite.enter_order_reference("1234")
        contactsite.enter_email_address("example13@mail.com")
        contactsite.click_send()
        time.sleep(1)
        msg_status = contactsite.check_returned_message_about_message_status_invalid_data()
        self.assertEqual(msg_status, "The message cannot be blank.")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()