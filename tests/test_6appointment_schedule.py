import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time

@allure.description("Verify the user can schedule the appoitnement")
@allure.severity(allure.severity_level.CRITICAL)
class Test_schedule_appoitment(Browser_initilize):

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_login(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Verify user is redirects to the appointment schedule page")
    def test_user_redirects_to_the_schedule_appointment_page(self):
        schedule_appointment_btn_xpath = helper.get_xpath(self, 'APPOINTMENT_SCHEDULE_BTN')
        manage_appointment_btn_xpath = helper.get_xpath(self, 'MANAGE_APPOINTMENTS_BTN')
        manage_appointment_title_xpath = helper.get_xpath(self, 'MANAGE_APPOINTMENT_TITLE')
        helper.wait_and_click(self, schedule_appointment_btn_xpath)
        assert helper.is_element_displayed(self, manage_appointment_btn_xpath)
        helper.wait_and_click(self, manage_appointment_btn_xpath)
        assert helper.is_element_displayed(self, manage_appointment_title_xpath)

    @allure.description("Verify user is can schedule the appointment")
    def test_schedule_appointment(self):
        patient_search_txt_xpath = helper.get_xpath(self, 'FIND_PATIENT_SEARCH_FIELD')
        patient_search_result_xpath = helper.get_xpath(self, 'SEARCH_RESULT')
        patient_appointment_title_xpath = helper.get_xpath(self, 'PATIENT_APPOINTMENTS_TITLE')
        patient_name = helper.get_data_parameters(self, 'patient_name')
        helper.clear_and_send_keys(self, patient_search_txt_xpath, patient_name)
        helper.wait_and_click(self, patient_search_result_xpath)
        assert helper.is_element_displayed(self, patient_appointment_title_xpath)



