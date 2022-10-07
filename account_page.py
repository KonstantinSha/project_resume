from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Account_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    button_shop = "/html/body/div[2]/header/div[1]/nav/ul/li[1]/a"


    # Getters

    def get_button_shop(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_shop)))


    # Actions

    def click_button_shop(self):
        self.get_button_shop().click()
        print('Click button shop')


    # Methods

    def enter_main_page(self):
        with allure.step("Enter main page"):
            Logger.add_start_step(method='Enter_main_page')
            self.click_button_shop()
            self.assert_url("https://www.maxpedition.com/pages/search-results-page")
            Logger.add_end_step(url=self.driver.current_url, method='Enter_main_page')


