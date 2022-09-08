import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os.path import dirname
from os.path import abspath
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging
from selenium.webdriver.chrome.options import Options
import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()



@pytest.fixture(scope="class")
def driver_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1325x744")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    chrome_options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    web_driver = webdriver.Chrome((ChromeDriverManager().install()), options=chrome_options)
    web_driver.maximize_window()
    data = read_data()
    server_URL = "https://" + data["server"]
    mylogger.info("running website tests on automation server - " + server_URL)
    web_driver.get(server_URL)
    web_driver.implicitly_wait(30)
    xpath_obj = create_xpath_obj()
    web_driver_wait = WebDriverWait(web_driver, 20)
    request.cls.driver = web_driver, data, xpath_obj, mylogger, web_driver_wait
    yield
    web_driver.close()

# clear file
def clearfolder(mydir):
    try:
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, mydir)
        if os.path.exists(mydir):
            filelist = [f for f in os.listdir(mydir)]
            for f in filelist:
                os.remove(os.path.join(destinationFile, f))
    except:
        print("Temp folder not found")


# get parent path
def getPARENTPATH():
    """return the path of the parent directory of current file's directory """
    current_dir_path = dirname(abspath(__file__))
    path_sep = os.path.sep
    components = current_dir_path.split(path_sep)
    return current_dir_path


# copy the xpaths from the screens into a temp file
def create_xpaths_file(screenlist):
    # list of screens required for the flow
    directory = getPARENTPATH() + "/data/screens/"
    srcdir = getPARENTPATH() + "/data/temp/"
    if not os.path.exists(srcdir):
        os.makedirs(srcdir)
    fwritename = srcdir + "temp.data"
    fwrite = open(fwritename, 'w')
    # create the data string by adding open and close flower brackets to the beginning and end respectively
    startstr = "{\n"
    endstr = '"endofile":""'"\n}"
    fwrite.write(startstr)
    # merge all the xpaths to a temp file
    for screen in screenlist:
        fname = directory + screen
        try:
            fread = open(fname, 'r')
        except FileNotFoundError:
            return fname + "absent"
        for line in fread.readlines():
            fwrite.write(line)
    fwrite.write(endstr)
    fwrite.close()
    return fwritename


# create xpath obj
def create_xpath_obj():
    clearfolder("data/temp")

    # Get folder paths and read xpaths
    parentdir = getPARENTPATH()
    clearfolder(parentdir + "/data/temp")
    pathstr = parentdir + "/data/screens/"
    source = os.listdir(pathstr)
    fwritename = create_xpaths_file(source)

    if "absent" in fwritename:
        mylogger.critical("xpath file is missing")
        pytest.exit("xpath is missing")

    # If xpath structure is wrong
    try:
        fread = open(fwritename, 'r')
    except:
        mylogger.error("since xpath Temp file not found")
        pytest.exit('Exiting pytest - since xpath Temp file not found')

    # Load xpath data
    try:
        xpath_obj = json.load(fread)
        fread.close()
        os.remove(fwritename)
    except:
        mylogger.critical(
            "Wrong json structure. Check data in temp file, correct the xpaths, delete the temp file and run again")
        pytest.exit(
            "Wrong json structure. Check data in temp file, correct the xpaths, delete the temp file and run again")
    mylogger.info("xpath object is created")
    return xpath_obj


# read data from
def read_data():
    with open(os.getcwd() + '/data/data_parameters.json', 'r') as file:
        data = json.load(file)
    file.close()
    return data


@pytest.mark.usefixtures("driver_init")
class Browser_initilize:
    pass
