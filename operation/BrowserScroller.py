from unit.robot import Courser
import time as timer


class PageScroller(Courser):

    def main_func(self):
        self.driver.execute_script('window.scroll(0,999999);')
