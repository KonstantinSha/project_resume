import datetime
from selenium.webdriver.common.keys import Keys

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url =self.driver.current_url
        print('Current url ' + get_url)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot("C:/Users/ASUS/Desktop/PythonQA4/Project_resume/screenshot/" + name_screenshot)

    """Method scroll down 600"""

    def scroll_down_600(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        print("Good scroll down 600")

    """Method scroll down 300"""

    def scroll_down_300(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Good scroll down 300")

    """Method Keys DOWN"""

    def click_keys_down(self):
        self.driver.send_keys(Keys.DOWN)
        print('Click keys down')

    """Method Keys Return"""

    def click_keys_return(self):
        self.driver.send_keys(Keys.RETURN)
        print('Click keys return')
