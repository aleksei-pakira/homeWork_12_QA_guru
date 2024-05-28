
from selene import browser, command


class SimpleRegistrationForm:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')
        self.output = browser.all('#output p')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_current_address(self, value):
        self.current_address.type(value)

    def fill_permanent_address(self, value):
        self.permanent_address.type(value)

    def submit_form(self):
        self.submit.perform(command.js.scroll_into_view)
        self.submit.click()
