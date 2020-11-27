class mainPage():

    def __init__(self, driver):
        self.driver = driver

        self.contact_us_button_by_xpath = '/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a'

    def goToContactUs(self):
        self.driver.find_element_by_xpath(self.contact_us_button_by_xpath).click()