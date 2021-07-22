from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() 
phonenum = 13782820017
password = 123456

def register():
    browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[2]/button[2][@type='button']").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[1]/input[@type='text']").send_keys(phonenum)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[5]/input[@type='password']").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/span[6]/input[@type='password']").send_keys(password)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button[@type='button']").click()
    time.sleep(1)
    a = browser.switch_to.alert
    time.sleep(1)
    a.accept()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/button[@type='button']").click()


def login():
    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/span[1]/input[@type='text']").send_keys(phonenum)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/span[2]/input[@type='password']").send_keys(password)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[1][@type='button']").click()


def choice_goods():
    browser.find_element_by_xpath("//*[@id='components-layout-demo-custom-trigger']/section/main/main/div[2]/div/div[1]/main/div[2]/div[1]/div/div[1]/img[@alt='example']").click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='components-layout-demo-custom-trigger']/section/main/main/div[1]/div/div/div[3]/div/div[3]/div[1]/button[@type='button']").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[3]/button[@type='button']").click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="J_tLoginId"]').send_keys("fvhekx0211@sandbox.com")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="payPasswd_rsainput"]').send_keys("111111")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="J_newBtn"]/span').click()
    time.sleep(3)
    browser.get('http://114.116.213.123:8081')


def show_user():
    browser.get('http://114.116.213.123:8081/#/user')
    time.sleep(2)
    browser.find_element_by_link_text('查看订单').click()
    time.sleep(2)
    browser.find_element_by_class_name('ant-modal-close-x').click()


def searche():
    browser.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/section/header/div/section/main/ul/span[2]/input[@type="text"]').send_keys("rtx")
    time.sleep(3)
    browser.find_element_by_class_name('ant-input-suffix').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div/div[3]/div/div[1]/img[@alt="example"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[1]/div/div/div[3]/div/div[3]/div[3]/button[@type="button"]').click()
    time.sleep(2)
    browser.get('http://114.116.213.123:8081/#/user')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/section/main/main/div[2]/div/div[2]/div/div[1]/div[1][@role="button"]').click()







if __name__ == "__main__":
    browser.get('http://114.116.213.123:8081')
    time.sleep(1)
    register()
    time.sleep(2)
    login()
    time.sleep(2)
    choice_goods()
    time.sleep(3)
    show_user()
    time.sleep(3)
    searche()