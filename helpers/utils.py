from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import requests

def get_driver(self):
    driver = self.driver[0]
    return driver


def get_server(self):
    data = self.driver[1]
    server_name = data["server"]
    return server_name


def get_logger(self):
    logger = self.driver[3]
    return logger


def get_page_title(self):
    page_title = get_driver(self).title
    return page_title


def get_xpath(self, xpath_value):
    xpath_obj = self.driver[2]
    xpath = xpath_obj[xpath_value]
    return xpath

def get_web_element_wait(self):
    wait = self.driver[4]
    return wait

def get_data_parameters(self, key):
    value = self.driver[1]
    return value[key]

def send_keys_action(element):
    element.send_keys(Keys.ENTER)


def clear_and_send_keys(self, xpath, value):
    wait = get_web_element_wait(self)
    driver = get_driver(self)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
    el_text_box = driver.find_element(By.XPATH, xpath)
    get_logger(self).info("enter value -> ({}) in text box -> {}, ".format(xpath, value))
    el_text_box.clear()
    el_text_box.send_keys(value)
    time.sleep(1)
    return el_text_box


# def select_element_from_drop_down(self, xpath, select_value, select_dropdown_by="visible_text"):
#     wait = get_web_element_wait(self)
#     driver = get_driver(self)
#     el_fish_name_drop_down = Select(driver.find_element(By.XPATH, xpath))
#     if select_dropdown_by == "visible_text":
#         el_fish_name_drop_down.select_by_visible_text(select_value)
#     driver.implicitly_wait(1)

def select_element_from_drop_down(self, xpath, value):
    wait = get_web_element_wait(self)
    driver = get_driver(self)
    x = Select(driver.find_element(By.XPATH, xpath))
    x.select_by_visible_text(value)



def alert_action(self, action="ok".upper()):
    driver = get_driver(self)
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)


def wait_and_click(self, xpath, action=None) -> bool:
    wait = get_web_element_wait(self)
    driver = get_driver(self)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
    el = driver.find_element(By.XPATH, xpath)
    el_isdisplayed = el.is_displayed()
    if action is None:
        el.click()
    elif action == "execute_script":
        driver.execute_script("arguments[0].click();", el)
    return el_isdisplayed


def get_element_attr_text(self, xpath, attr=None):
    wait = get_web_element_wait(self)
    driver = get_driver(self)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
    el = driver.find_element(By.XPATH, xpath)
    if attr == "get_price":
        text_attr = el.text
        text_attr = round(float(''.join(re.findall(r"[-+]?\d*\.\d+|\d+", text_attr))), 2)
    elif attr == "value":
        text_attr = el.get_attribute('value')
    elif attr == "title":
        text_attr = el.get_attribute('title')
    else:
        text_attr = el.text

    get_logger(self).info("element attribute of -> {} is -> {}".format(xpath, text_attr))
    return text_attr


def navigate_back(self):
    driver = get_driver(self)
    driver.execute_script("window.history.go(-1)")
    return navigate_back


def refresh_browser(self):
    driver = get_driver(self)
    driver.refresh()

def driver_wait(self):
    driver = get_driver(self)
    driver.implicitly_wait(10)

def is_element_displayed(self, xpath):
    driver = get_driver(self)
    wait = get_web_element_wait(self)
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        el = driver.find_element_by_xpath(xpath)
        element = el.is_displayed()
        return element
    except:
        get_logger(self).error("element is not found - {}".format(xpath))
        return False

