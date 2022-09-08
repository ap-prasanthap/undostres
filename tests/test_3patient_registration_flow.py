import allure

import helpers.utils as helper
from set_up import Browser_initilize
import helpers.common_actions as commonmethods
import time



@allure.description("Verify the patient registration functionality")
@allure.severity(allure.severity_level.CRITICAL)
class Test_patient_registration_functionality(Browser_initilize):

    @allure.description("Verify the user is able to login by using the valid credentials")
    def test_login(self):
        username = helper.get_data_parameters(self, 'username')
        password = helper.get_data_parameters(self, 'password')
        # login with valid credentials
        commonmethods.login(self,username,password)

    @allure.description("Verify the patient registration page displayed")
    def test_patient_registration_page_displayed(self):
        patient_registration_btn_xpath = helper.get_xpath(self, 'REGISTER_PATIENT_BTN')
        helper.wait_and_click(self, patient_registration_btn_xpath)
        actual_title = helper.get_page_title(self)
        assert "OpenMRS Electronic Medical Record" in actual_title, "User is not redirected to the Registration screen"

    @allure.description("Verify the demographics name fields with valid data")
    def test_user_can_fill_names_in_demographics_details_with_valid_values(self):
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        given_name = helper.get_data_parameters(self, 'given_name')
        middle_name = helper.get_data_parameters(self, 'middle_name')
        family_name = helper.get_data_parameters(self, 'family_name')
        commonmethods.demographics_fill_names(self, given_name, middle_name, family_name)
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the user can select the gender")
    def test_user_can_select_the_gender(self):
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        gender_btn_xpath = helper.get_xpath(self, 'GENDER_BTN')
        helper.wait_and_click(self, gender_btn_xpath)
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the user can select the date of birth")
    def test_user_can_enter_the_dob(self):
        day_xpath = helper.get_xpath(self, 'DAY_TXT')
        month_xpath = helper.get_xpath(self, 'MONTH')
        year_xpath = helper.get_xpath(self, 'YEAR_TXT')
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        helper.clear_and_send_keys(self, day_xpath, "8")
        helper.select_element_from_drop_down(self, month_xpath, "February")
        helper.clear_and_send_keys(self, year_xpath, "1986")
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the user can fill the address details")
    def test_user_can_enter_the_address_details(self):
        address1 = helper.get_data_parameters(self, 'address1')
        address2 = helper.get_data_parameters(self, 'address2')
        village_name = helper.get_data_parameters(self, 'village_name')
        state_name = helper.get_data_parameters(self, 'state_name')
        country_name = helper.get_data_parameters(self, 'country_name')
        postal_code = helper.get_data_parameters(self, 'postal_code')
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        commonmethods.add_address(self, address1, address2, village_name, state_name, country_name, postal_code)
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the user can enter the phone number")
    def test_user_can_enter_the_phone_number(self):
        phone_number_xpath = helper.get_xpath(self, 'PHONE_NUMBER_TXT')
        phone_number = helper.get_data_parameters(self, 'phone_number')
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        helper.clear_and_send_keys(self, phone_number_xpath, phone_number)
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the user can enter the relation to the patient")
    def test_user_can_enter_relation(self):
        relation_type_xpath = helper.get_xpath(self, 'RELATION_TYPE')
        relation_person_name_xpath = helper.get_xpath(self, 'RELATION_PERSON_NAME_TXT')
        next_btn_xpath = helper.get_xpath(self, 'NEXT_BTN')
        relative_name = helper.get_data_parameters(self, 'relative_name')
        helper.select_element_from_drop_down(self, relation_type_xpath, 'Sibling' )
        helper.clear_and_send_keys(self, relation_person_name_xpath, relative_name)
        helper.wait_and_click(self, next_btn_xpath)

    @allure.description("Verify the patient registration is successful")
    def test_registration(self):
        submit_btn_xpath = helper.get_xpath(self, 'SUBMIT_BTN')
        patient_given_name_xpath = helper.get_xpath(self, 'PATIENT_GIVEN_NAME')
        patient_family_name_xpath = helper.get_xpath(self, 'PATIENT_FAMILY_NAME')
        given_name = helper.get_data_parameters(self, 'given_name')
        family_name = helper.get_data_parameters(self, 'family_name')
        helper.wait_and_click(self, submit_btn_xpath)
        patient_given_name = helper.get_element_attr_text(self,patient_given_name_xpath)
        patient_family_name = helper.get_element_attr_text(self,patient_family_name_xpath)
        assert given_name == patient_given_name, "Given name displayed is wrong"
        assert family_name == patient_family_name, "Family name displayed is wrong"
