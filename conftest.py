import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_experimental_option("prefs",
                                    {"download.default_directory": os.getcwd(),
                                     "download.prompt_for_download": False,
                                     "download.directory_upgrade": True,
                                     "safebrowsing.enabled": True
                                     })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
