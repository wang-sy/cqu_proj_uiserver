import time

import tool

# run this in index
def registry(browser, user, time_step):
    """
    registry a user
    :param time_step: wait time after each action
    :param browser: browser
    :param user: dict() with phone_number, username, password, email, address
    """
    tool.get_element_by_xpath(browser, "/html/body/div/div/div[2]/div/div[2]/div[2]/button[2][@type='button']", time_step).click()
    tool.get_element_by_xpath(browser, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[1]/input[@type='text']", time_step).send_keys(user["phone_number"])
    tool.get_element_by_xpath(browser, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[5]/input[@type='password']", time_step).send_keys(user["password"])
    tool.get_element_by_xpath(browser, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[6]/input[@type='password']", time_step).send_keys(user["password"])
    tool.get_element_by_xpath(browser, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button[@type='button']", time_step).click()
    time.sleep(time_step)
    a = browser.switch_to.alert
    a.accept()


def login(browser, user, time_step):
    """
    do login for user
    :param time_step: wait time after each action
    :param browser: browser
    :param user: dict() with phone_number, username, password, email, address
    """
    tool.get_element_by_xpath(browser, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/span[1]/input[@type='text']", time_step).send_keys(user["phone_number"])
    tool.get_element_by_xpath(browser, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/span[2]/input[@type='password']", time_step).send_keys(user["password"])
    tool.get_element_by_xpath(browser, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[1][@type='button']", time_step).click()
