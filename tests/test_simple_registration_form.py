import allure
from allure_commons.types import Severity
from selene import have

from demoqa_tests.application import app
from demoqa_tests.data import users


@allure.label('owner', 'aleksei-pakira')
@allure.feature('Simple registration form')
@allure.story('User should be able to register via simple registration form')
@allure.title('Registered data match the data indicated while registering')
@allure.severity(Severity.BLOCKER)
def test_simple_registration_form():
    user = users.admin

    with allure.step('Open simple registration form from the left panel'):
        app.left_panel.open_simple_registration_form()

    with allure.step('Fill the simple registration form'):
        app.simple_registration.fill_full_name(f'{user.first_name} {user.last_name}')
        app.simple_registration.fill_email(user.email)
        app.simple_registration.fill_current_address(user.current_address)
        app.simple_registration.fill_permanent_address(user.permanent_address)

    with allure.step('Submit the simple registration form'):
        app.simple_registration.submit_form()

    with allure.step('Check the data of the registered user'):
        app.simple_registration.output.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.current_address,
            user.permanent_address
        )
        )