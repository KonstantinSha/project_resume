from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = "//input[@type='email']"
    password = "//input[@type='password']"
    button_enter = "//input[@type='submit']"


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_enter)))


    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_button_enter(self):
        self.get_button_enter().click()
        print('Click button enter')


    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method='authorization')
            self.input_user_name('test9378911@gmail.ru')
            self.input_password('aser4567aser4567')
            self.click_button_enter()
            # self.assert_url("https://www.maxpedition.com/account")
            # time.sleep(3)
            Logger.add_end_step(url=self.driver.current_url, method='authorization')


