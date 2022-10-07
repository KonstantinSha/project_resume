import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkbutton_backpack = "//*[@id='snize_filters_block_product_type']/ul/li[3]/label/div"
    product_name = "//*[@id='snize-product-8400941969']/a/div/span/span[1]"
    product_price = "//*[@id='snize-product-8400941969']/a/div/span/div/span"
    product = "//*[@id='snize-product-8400941969']/a/div/div/span/img"


    # Getters

    def get_checkbutton_backpack(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.checkbutton_backpack)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.product)))

    # Actions

    def click_checkbutton_backpack(self):
        self.get_checkbutton_backpack().click()
        print('Click checkbutton backpack')

    def read_product_name(self):
        value_product_name = self.get_product_name().text
        print(value_product_name)

    def read_product_price(self):
        value_product_price = self.get_product_price().text
        print(value_product_price)

    def click_product(self):
        self.get_product().click()
        print('Click product')

    # Methods

    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            self.click_checkbutton_backpack()
            time.sleep(3)
            self.scroll_down_600()
            time.sleep(2)
            self.read_product_name()
            self.read_product_price()
            self.click_product()
            self.get_current_url()
            self.assert_url('https://www.maxpedition.com/products/lithvore-everyday-backpack?variant=28168844369')
            Logger.add_end_step(url=self.driver.current_url, method='select_product')



