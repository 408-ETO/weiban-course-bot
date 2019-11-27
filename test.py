from selenium import webdriver
import time as timer
from operation.login import AccoutLoginer as Loginer
from operation.watchVideo import VideoWatcher

driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()

info = ['天津大学','3018233061','3018233061']
loginer = Loginer(driver,info)
loginer.process()

timer.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div').click()

timer.sleep(1)
target_ul = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[5]/div/div[1]/div/div[3]/ul/li[5]')
driver.execute_script('arguments[0].click()',target_ul)

vwer = VideoWatcher(driver)
vwer.process()
