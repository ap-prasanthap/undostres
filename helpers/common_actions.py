import time
import helpers.utils as helper
from set_up import Browser_initilize


def login(self, username, password):
    login_username_xpath = helper.get_xpath(self, 'USERNAME_TXT_FIELD')
    login_password_xpath = helper.get_xpath(self, 'PASSWORD_TXT_FIELD')
    login_button_xpath = helper.get_xpath(self, 'LOGIN_BTN')
    location_xpath = helper.get_xpath(self, 'LOCATION')
    helper.clear_and_send_keys(self, login_username_xpath, username)
    helper.clear_and_send_keys(self, login_password_xpath, password)
    helper.wait_and_click(self, location_xpath)
    helper.wait_and_click(self, login_button_xpath)


def demographics_fill_names(self, given_name, middle_name, family_name):
    given_name_xpath = helper.get_xpath(self, 'GIVEN_NAME')
    middle_name_xpath = helper.get_xpath(self, 'MIDDLE_NAME')
    family_name_xpath = helper.get_xpath(self, 'FAMILY_NAME')
    helper.clear_and_send_keys(self, given_name_xpath, given_name)
    helper.clear_and_send_keys(self, middle_name_xpath, middle_name)
    helper.clear_and_send_keys(self, family_name_xpath, family_name)


def add_address(self, address1, address2, village, state, country, postcode):
    address1_xpath = helper.get_xpath(self, 'ADDRESS1_TXT')
    address2_xpath = helper.get_xpath(self, 'ADDRESS2_TXT')
    village_xpath = helper.get_xpath(self, 'VILLAGE_TXT')
    state_xpath = helper.get_xpath(self, 'STATE_TXT')
    country_xpath = helper.get_xpath(self, 'COUNTRY_TXT')
    postal_code_xpath = helper.get_xpath(self, 'POSTAL_CODE_TXT')

    helper.clear_and_send_keys(self, address1_xpath, address1)
    helper.clear_and_send_keys(self, address2_xpath, address2)
    helper.clear_and_send_keys(self, village_xpath, village)
    helper.clear_and_send_keys(self, state_xpath, state)
    helper.clear_and_send_keys(self, country_xpath, country)
    helper.clear_and_send_keys(self, postal_code_xpath, postcode)

