import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the login functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_login_functionality(Browser_initilize):

    @allure.description("Verify the page title to ensure that the user is redirected to the login screen")
    def test_user_launched_into_the_login_page(self):
        actual_title = helper.get_page_title(self)
        assert "Login" in actual_title, "User is not redirected to the login screen"

    @allure.description("Verify the username and password fields with a Login button is displayed in the login screen")
    def test_required_text_fields_are_displayed(self):
        login_username_xpath = helper.get_xpath(self, 'USERNAME_TXT_FIELD')
        login_password_xpath = helper.get_xpath(self, 'PASSWORD_TXT_FIELD')
        login_button_xpath = helper.get_xpath(self, 'LOGIN_BTN')
        # Verifying the fields are displayed
        assert helper.is_element_displayed(self, login_username_xpath), "Username field is missing"
        assert helper.is_element_displayed(self, login_password_xpath), "Password field is missing"
        assert helper.is_element_displayed(self, login_button_xpath), "Login button is missing"

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_user_logged_in_with_valid_credentials(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Verify the user is redirected to the home page")
    def test_user_is_redirected_to_the_home_page_after_login(self):
        logged_in_user_info_xpath = helper.get_xpath(self, 'LOGGED_IN_USER_INFO')
        actual_logged_in_user_info = helper.get_element_attr_text(self, logged_in_user_info_xpath)
        expected_logged_in_user_info = helper.get_data_parameters(self, 'expected_logged_in_user_info')
        actual_title = helper.get_page_title(self)
        assert "Home" in actual_title, "User is not redirected to the login screen"
        assert actual_logged_in_user_info == expected_logged_in_user_info










