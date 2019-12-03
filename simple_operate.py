from selenium import webdriver
import time as timer
from operation.login import AccoutLoginer as Loginer
import re

# init driver
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()

info = ['天津大学', '3018233042', '3018233042']
# login
loginer = Loginer(driver, info)
loginer.process()

timer.sleep(1)
# click to enter the target course
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div[3]/div/div').click()

for i in range(75):
    # force to sleep for a healthy life
    timer.sleep(1)
    # get elements after rerender
    try:
        li = driver.find_element_by_xpath("//li[@class='listview-item']")
    except Exception as e:
        print(e)
        # if not able to find a active li then break the loop
        break
    # click to enter lesson of the <li> item
    driver.execute_script('arguments[0].click();', li)
    timer.sleep(1)
    # get url args
    url_args = re.findall(r'\?(.+)$', driver.current_url)
    # post finish msg to backend
    js = "window.fetch('https://weiban.mycourse.cn/pharos/usercourse/finish.do?{}')".format(
        url_args[0])
    driver.execute_script(js)
    timer.sleep(1)
    # navigate back
    driver.back()
