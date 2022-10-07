from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Start_page(Base):

    url = 'https://www.maxpedition.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    button_x = "/html/body/div[5]/a"
    button_login = "/html/body/div[2]/header/div/ul/li[1]/a"


    # Getters

    def get_button_x(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_x)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_login)))


    # Actions

    def click_button_x(self):
        self.get_button_x().click()
        print('Click button x')

    def click_button_login(self):
        self.get_button_login().click()
        print('Click button login')


    # Methods

    def enter_login_page(self):
        with allure.step("Enter login page"):
            Logger.add_start_step(method='enter_login_page')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button_x()
            self.click_button_login()
            self.assert_url("https://www.maxpedition.com/account/login")
            Logger.add_end_step(url=self.driver.current_url, method='enter_login_page')


