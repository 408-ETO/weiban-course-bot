from selenium import webdriver
import pytesseract
from PIL import Image
import re
import time as timer


class AccoutLoginer:
    def __init__(self, driver, info=[]):
        self.driver = driver
        self.info = info

    def process(self):
        self.driver.get('http://weiban.mycourse.cn/#/login')
        self.__input_info()

    # default code-img download path
    __img_path = './temp/code-img.png'

    # solve_code_img
    def __handle_code_img(self):
        while True:
            img_element = self.driver.find_element_by_css_selector(
                'img.code-img')
            # screenshot code-img
            img_element.screenshot(self.__img_path)
            try:
                # recognize text from screenshot
                text = pytesseract.image_to_string(Image.open(self.__img_path))
                # regex number and sign from text
                args = re.findall(r'(\d+).*([+-]{1}).*(\d+)', text)
                print(args)
                arg1, sign, arg2 = args[0]
                # calculate code-img result from args
                result = int(arg1) + (1 if sign == '+' else -1) * int(arg2)
                return result
            except Exception:
                # click code-img to change code for next try
                img_element.click()
                print('code-img', 'try again')

    # input user info for login
    def __input_info(self):
        # tab to login with user account and password mode
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/a[2]').click()
        info = self.info[0:3]
        info.append(self.__handle_code_img())
        # find all input elements
        els = self.driver.find_elements_by_css_selector('.form-item input')
        # input user-info with loop
        for i, el in enumerate(els):
            el.send_keys(info[i])
        self.__go_login()

    def __go_login(self):
        timer.sleep(2)
        try:
            # handle popup-msgbox
            alert_bn = self.driver.find_element_by_css_selector(
                '.mint-msgbox-confirm')
            self.driver.execute_script('arguments[0].click();', alert_bn)
        except Exception:
            print('login without msgbox-confirm')
        timer.sleep(2)
        # tap login-button
        login_bn = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[3]/div/div[2]/div/div[1]/button/label')
        self.driver.execute_script('arguments[0].click();', login_bn)
