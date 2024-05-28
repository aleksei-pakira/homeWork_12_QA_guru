
import datetime
from pathlib import Path
from selene import browser, have, by, command

import tests


class RegistrationForm:

    def __init__(self):
        self.registered_data = browser.element('.table').all('td').even

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def select_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def fill_birth_date(self, year, month, day):
        birth_date = datetime.date(year, month, day)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(by.text(f'{birth_date.year}')).click()
        (browser.element('.react-datepicker__month-select').click().
         element(by.text(f'{birth_date.strftime('%B')}')).click())
        browser.element(f'.react-datepicker__day--0{birth_date.day}').click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobby(self, hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).perform(command.js.scroll_into_view).click()

    def upload_picture(self, file):
        (browser.element('#uploadPicture').
         set_value(str(Path(tests.__file__).parent.joinpath(f'resources/{file}').absolute())
                   ))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def select_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select]').element_by(have.text(state)).click()

    def select_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select]').element_by(have.text(city)).click()

    def submit_form(self):
        browser.element('#submit').click()
