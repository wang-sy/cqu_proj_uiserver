from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element_by_xpath(browser, path, timeout=10) -> object:
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
