import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the view patient record functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_view_patient_functionality(Browser_initilize):

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_login(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Find a patient record")
    def test_find_a_patient_record(self):
        find_patient_record_btn_xpath = helper.get_xpath(self, 'FIND_PATIENT_RECORD_BTN')
        patient_search_txt_xpath = helper.get_xpath(self, 'FIND_PATIENT_SEARCH_FIELD')
        helper.wait_and_click(self, find_patient_record_btn_xpath)
        patient_name = helper.get_data_parameters(self, 'patient_name')
        helper.clear_and_send_keys(self, patient_search_txt_xpath, patient_name)
        patient_search_result_xpath = helper.get_xpath(self, 'SEARCH_RESULT')
        helper.wait_and_click(self, patient_search_result_xpath)

    @allure.description("Find a patient record")
    def test_assert_patient_details(self):
        patient_given_name_xpath = helper.get_xpath(self, 'PATIENT_GIVEN_NAME')
        patient_family_name_xpath = helper.get_xpath(self, 'PATIENT_FAMILY_NAME')
        patient_middle_name_xpath = helper.get_xpath(self, 'PATIENT_MIDDLE_NAME')
        patient_gender_xpath = helper.get_xpath(self, 'PATIENT_GENDER')
        patient_contact_number_xpath = helper.get_xpath(self, 'PHONE_NUMBER_TXT')
        contact_info_xpath = helper.get_xpath(self, 'CONTACT_INFO_BTN')
        given_name = helper.get_data_parameters(self, 'given_name')
        middle_name = helper.get_data_parameters(self, 'middle_name')
        family_name = helper.get_data_parameters(self, 'family_name')
        contact_number = helper.get_data_parameters(self, 'phone_number')
        helper.wait_and_click(self, contact_info_xpath)
        patient_given_name = helper.get_element_attr_text(self, patient_given_name_xpath)
        patient_family_name = helper.get_element_attr_text(self, patient_family_name_xpath)
        patient_middle_name = helper.get_element_attr_text(self, patient_middle_name_xpath)
        patient_gender = helper.get_element_attr_text(self, patient_gender_xpath)
        # patient_contact_number = helper.get_element_attr_text(self, patient_contact_number_xpath)
        assert given_name == patient_given_name
        assert middle_name == patient_middle_name
        assert family_name == patient_family_name
        # assert contact_number == patient_contact_number
        assert "Male" in patient_gender, "User is not redirected to the login screen"
