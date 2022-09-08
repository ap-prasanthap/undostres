import pytest
from pytest import fixture
from set_up import driver_init
import os
import allure
from allure import attachment_type
from os import path
from typing import Any, Callable, Optional

from _pytest.fixtures import SubRequest
from pytest import fixture

ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    attaches screenshot to the report when test fails
    '''
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'request' in item.fixturenames:
                    web_driver = ((getattr(item.obj, '__self__', None)).driver)[0]
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

@fixture(scope='session', autouse=True)
def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:

    environment_properties = dict()

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption(ALLUREDIR_OPTION)

    if not alluredir or not path.isdir(alluredir) or not environment_properties:
        return

    allure_env_path = path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)

    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)

@fixture(autouse=True)
def cenpprop(add_allure_environment_property: Callable) -> None:
    add_allure_environment_property('Browser', 'Chrome')
    add_allure_environment_property('Url', 'https://tree.taiga.io/discover')

