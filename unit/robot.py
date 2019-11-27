import time as timer

class Courser:
    def __init__(self, driver):
        self.driver = driver

    def __before_start(self):
        # fix main window handle
        self.main_handle = self.driver.current_window_handle

    def process(self):
        self.__before_start()
        timer.sleep(2)
        self.main_func()
        timer.sleep(2)
        self.__on_finish()

    def main_func(self):
        pass

    def __on_finish(self):
        # handle alert
        self.driver.switch_to.alert.accept()
        # switch back
        self.driver.switch_to.window(self.main_handle)
        # navigate back
        self.driver.back()
