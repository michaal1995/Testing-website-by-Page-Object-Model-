class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_address_textbox_by_id = "email"
        self.order_reference_textbox_by_id = "id_order"
        self.text_messagebox_by_id = "message"
        self.send_button_by_id = "submitMessage"
        self.subject_heading_box_by_xpath = \
            "/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/div[1]/div"
        self.message_status_text_by_css_selector = '#center_column > p'
        self.message_status_error_by_xpath = '//*[@id="center_column"]/div/ol/li'

    def enter_email_address(self, email_address):
        self.driver.find_element_by_id(self.email_address_textbox_by_id).clear()
        self.driver.find_element_by_id(self.email_address_textbox_by_id).send_keys(email_address)

    def enter_order_reference(self, order_reference):
        self.driver.find_element_by_id(self.order_reference_textbox_by_id).clear()
        self.driver.find_element_by_id(self.order_reference_textbox_by_id).send_keys(order_reference)

    def enter_text_message(self, text_message):
        self.driver.find_element_by_id(self.text_messagebox_by_id).clear()
        self.driver.find_element_by_id(self.text_messagebox_by_id).send_keys(text_message)

    def click_send(self):
        self.driver.find_element_by_id(self.send_button_by_id).click()

    def set_subject_heading_as_customer_service(self):
        self.driver.find_element_by_xpath(self.subject_heading_box_by_xpath).click()
        choose = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/div[1]/div')
        choose.click()
        setvalue = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/div[1]/div/select')
        setvalue.send_keys('\ue015')
        setvalue.send_keys('\ue007')

    def check_returned_message_about_message_status_valid_data(self):
        status_message = self.driver.find_element_by_css_selector(self.message_status_text_by_css_selector).text
        return status_message

    def check_returned_message_about_message_status_invalid_data(self):
        status_message = self.driver.find_element_by_xpath(self.message_status_error_by_xpath).text
        return status_message
