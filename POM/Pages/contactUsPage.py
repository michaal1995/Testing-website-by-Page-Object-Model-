class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_address_textbox_by_id = "email"
        self.order_reference_textbox_by_id = "id_order"
        self.text_messagebox_by_id = "message"
        self.send_button_by_id = "submitMessage"

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


