import tool
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


ORDER_MODAL_SUBMIT_BUTTON = """/html/body/div/div/div[2]/div/div[2]/div[3]/button"""
ALIPAY_EMAIL_INPUT = """//*[@id="J_tLoginId"]"""
ALIPAY_PASSWORD_INPUT = """//*[@id="payPasswd_rsainput"]"""
ALIPAY_LOGIN_BUTTON = """//*[@id="J_newBtn"]/span"""


def goto_alipay(browser):
    button = tool.get_element_by_xpath(browser, ORDER_MODAL_SUBMIT_BUTTON)
    button.click()


def do_alipay(browser):
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="J_tLoginId"]').send_keys("fvhekx0211@sandbox.com")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="payPasswd_rsainput"]').send_keys("111111")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="J_newBtn"]/span').click()