import time as timer
from unit.robot import Courser

class VideoWatcher(Courser):

    def main_func(self):
        # switch to video frame
        self.driver.switch_to.frame('video_iframe')
        video_el = self.driver.find_element_by_css_selector('video')
        # finish video directly by injecting js
        self.driver.execute_script('arguments[0].currentTime = arguments[0].duration',video_el)
        # wait for alert
        timer.sleep(1)
