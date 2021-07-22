from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://localhost:8080/')
time.sleep(6)
# browser.find_element_by_xpath("//input[@placeholder='电话']").send_keys("aaaaaaaaaa")
# time.sleep(1)
# browser.find_element_by_xpath("//input[@placeholder='密码']").send_keys("111111")
# time.sleep(1)
# browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[2]/button[1][@type='button']").click()

browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/button[@type='button']").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='components-layout-demo-custom-trigger']/section/main/main/div[2]/div/div[1]/main/div[2]/div[1]/div/div[1][@class='ant-card-cover']").click()
