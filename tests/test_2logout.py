import allure
import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the logout functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_logout_functionality(Browser_initilize):

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_login(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Verify the user can logout")
    def test_logout(self):
        logged_in_user_info_xpath = helper.get_xpath(self, 'LOGOUT_BTN')
        helper.wait_and_click(self, logged_in_user_info_xpath)

    @allure.description("Verify the user is redirected to the login page after logout")
    def test_user_is_redirected_to_login_page(self):
        actual_title = helper.get_page_title(self)
        assert "Login" in actual_title, "User is not redirected to the login screen"










