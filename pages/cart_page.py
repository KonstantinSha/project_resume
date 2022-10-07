import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_prtotection_close = "//*[@id='speakerPower']"
    cart_product_name = "//*[@id='sca_fg_cart']/div[1]/div/form/table[2]/tbody/tr[1]/td[2]/a"
    cart_product_price = "//*[@id='sca_fg_cart']/div[1]/div/form/table[2]/tbody/tr/td[3]/span"
    subtotal_price = "//*[@id='sca_fg_cart']/div[1]/div/form/p[1]/span[1]"
    button_debit_or_credit_card = "//*[@id='sca_fg_cart']/div[1]/div/form/div[2]/input"

    # Getters

    def get_button_prtotection_close(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_prtotection_close)))

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_product_name)))

    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_product_price)))

    def get_subtotal_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.subtotal_price)))

    def get_button_debit_or_credit_card(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_debit_or_credit_card)))

    # Actions

    def click_button_prtotection_close(self):
        self.get_button_prtotection_close().click()
        print('Click button button prtotection close')

    def read_cart_product_name(self):
        value_cart_product_name = self.get_cart_product_name().text
        print(value_cart_product_name)

    def read_cart_product_price(self):
        value_cart_product_price = self.get_cart_product_price().text
        print(value_cart_product_price)
        return value_cart_product_price

    def read_subtotal_price(self):
        value_subtotal_price = self.get_subtotal_price().text
        print(value_subtotal_price)
        assert value_subtotal_price == self.read_cart_product_price()
        print ("Price subtotal GOOD")

    def click_button_debit_or_credit_card(self):
        self.get_button_debit_or_credit_card().click()
        print('Click button debit or credit card')

    # Methods

    def transition_to_payment(self):
        with allure.step("Transition to payment"):
            Logger.add_start_step(method='transition_to_payment')
            self.click_button_prtotection_close()
            time.sleep(5)
            self.read_cart_product_name()
            self.read_cart_product_price()
            self.read_subtotal_price()
            self.click_button_debit_or_credit_card()
            Logger.add_end_step(url=self.driver.current_url, method='transition_to_payment')



