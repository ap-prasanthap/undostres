import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the find patient functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_find_patient_functionality(Browser_initilize):

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_login(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Verify the patient registration page displayed")
    def test_find_patient_page_displayed(self):
        find_patient_record_btn_xpath = helper.get_xpath(self, 'FIND_PATIENT_RECORD_BTN')
        helper.wait_and_click(self, find_patient_record_btn_xpath)
        actual_title = helper.get_page_title(self)
        assert "OpenMRS Electronic Medical Record" in actual_title, "User is not redirected to the patient search screen"

    @allure.description("Verify the patient search")
    def test_patient_search_field(self):
        patient_search_txt_xpath = helper.get_xpath(self, 'FIND_PATIENT_SEARCH_FIELD')
        patient_search_result_xpath = helper.get_xpath(self, 'SEARCH_RESULT')
        patient_name = helper.get_data_parameters(self, 'patient_name')
        helper.clear_and_send_keys(self, patient_search_txt_xpath, patient_name)
        assert helper.is_element_displayed(self, patient_search_result_xpath), 'Search result is not found'

    @allure.description("Verify the user is redirects to the patient page")
    def test_user_is_redirected_to_the_patient_page(self):
        patient_search_result_xpath = helper.get_xpath(self, 'SEARCH_RESULT')
        helper.wait_and_click(self, patient_search_result_xpath)
        actual_title = helper.get_page_title(self)
        assert "OpenMRS Electronic Medical Record" in actual_title, "User is not redirected to the patient screen"
