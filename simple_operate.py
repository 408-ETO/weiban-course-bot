from selenium import webdriver
import time
from operation.login import AccoutLoginer as Loginer
import re

# init driver
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()

account = '3018233060'

# login
loginer = Loginer(driver=driver, info=['天津大学', account, account])
loginer.process()

time.sleep(1)
# click to enter the target course
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div[3]/div/div').click()

for i in range(75):
    # force to sleep for a healthy livelihood
    time.sleep(1)

    # get elements after rerender
    try:
        li = driver.find_element_by_xpath("//li[@class='listview-item']")
    except Exception as e:
        print(e)
        # if not able to find a active li then break the loop
        break

    # click to enter lesson in the <li> item
    driver.execute_script('arguments[0].click();', li)
    time.sleep(1)

    # get url args
    url_args = re.findall(r'\?(.+)$', driver.current_url)[0]
    # post finish msg to backend
    js = "window.fetch('https://weiban.mycourse.cn/pharos/usercourse/finish.do?{}')".format(
        url_args)
    # post with js:fetch()
    driver.execute_script(js)
    print('post ~args:{}'.format(url_args))
    time.sleep(1)

    # navigate back
    driver.back()

print('progress end')
