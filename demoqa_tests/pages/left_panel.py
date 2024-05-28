
from selene import browser, have


class LeftPanel:

    def open(self, value_1, value_2):
        browser.open('/')
        browser.all('.category-cards .card').element_by(have.text(value_1)).with_(timeout=6).click()
        browser.all('.left-pannel li').element_by(have.text(value_2)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')

    def open_registration_form(self):
        self.open('Forms', 'Practice Form')
