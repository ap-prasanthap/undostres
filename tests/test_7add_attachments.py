import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the user can add attachments to the patient")
@allure.severity(allure.severity_level.CRITICAL)
class Test_add_attachments_functionality(Browser_initilize):

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

    @allure.description("Verify user can add attachments")
    def test_add_attachments(self):
        attachments_btn_xpath = helper.get_xpath(self, 'ATTACHMENT_BTN')
        attachments_validation_message_xpath = helper.get_xpath(self, 'ATTACHMENT_VALIDATION_MESSAGE')
        helper.wait_and_click(self, attachments_btn_xpath)
        helper.is_element_displayed(self, attachments_validation_message_xpath)
