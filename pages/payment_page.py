import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Payment_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    payment_page_product_name = "//*[@id='order-summary']/div/div[1]/div/table/tbody/tr/th/span[1]"
    payment_page_product_price = "//*[@id='order-summary']/div/div[1]/div/table/tbody/tr/td[3]/span"
    payment_page_subtotal_price = "//*[@id='order-summary']/div/div[3]/table/tbody/tr[1]/td/span"
    total = "//span[@class='payment-due__price skeleton-while-loading--lg']"
    email = "//*[@id='checkout_email']"
    first_name = "//*[@id='checkout_shipping_address_first_name']"
    last_name = "//*[@id='checkout_shipping_address_last_name']"
    company = "//*[@id='checkout_shipping_address_company']"
    address_line_1 = "//*[@id='checkout_shipping_address_address1']"
    address_line_2 = "//*[@id='checkout_shipping_address_address2']"
    city = "//*[@id='checkout_shipping_address_city']"
    state = "//*[@id='checkout_shipping_address_province']"
    state_alabama = "//*[@id='checkout_shipping_address_province']/option[2]"
    zip_code = "//*[@id='checkout_shipping_address_zip']"
    phone = "//*[@id='checkout_shipping_address_phone']"
    button_continue = "//*[@id='continue_button']"


    # Getters

    def get_payment_page_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.payment_page_product_name)))

    def get_payment_page_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.payment_page_product_price)))

    def get_payment_page_subtotal_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.payment_page_subtotal_price)))

    def get_total(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.total)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.email)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_company(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.company)))

    def get_address_line_1(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.address_line_1)))

    def get_address_line_2(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.address_line_2)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.city)))

    def get_state(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.state)))

    def get_state_alabama(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.state_alabama)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.phone)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_continue)))


    # Actions

    def read_payment_page_product_name(self):
        value_payment_page_product_name = self.get_payment_page_product_name().text
        print(value_payment_page_product_name)

    def read_payment_page_product_price(self):
        value_payment_page_product_price = self.get_payment_page_product_price().text
        print(value_payment_page_product_price)

    def read_payment_page_subtotal_price(self):
        value_payment_page_subtotal_price = self.get_payment_page_subtotal_price().text
        print(value_payment_page_subtotal_price)
        return value_payment_page_subtotal_price

    def read_total(self):
        value_total = self.get_total().text
        print(value_total)
        assert value_total == self.read_payment_page_subtotal_price()
        print ("Price total GOOD")

    def click_email(self):

        self.get_email().click()
        self.get_email().send_keys("test9378911@gmail.ru")
        print('Click email + print test9378911@gmail.ru')

    def click_first_name(self):

        self.get_first_name().click()
        self.get_first_name().send_keys("Alex")
        print('Click first name + print Alex')

    def click_last_name(self):
        self.get_last_name().click()
        self.get_last_name().send_keys("Jons")
        print('Click last name + print Jons')

    def click_company(self):
        self.get_company().click()
        self.get_company().send_keys("Sony")
        print('Click company + print Sony')

    def click_address_line_1(self):
        self.get_address_line_1().click()
        self.get_address_line_1().send_keys("street 1")
        print('Click address line 1 + print street 1')

    def click_address_line_2(self):
        self.get_address_line_2().click()
        self.get_address_line_2().send_keys("street 2")
        print('Click address line 2 + print street 2')

    def click_city(self):
        self.get_city().click()
        self.get_city().send_keys("New York")
        print('Click city + print New York')

    def click_state(self):
        self.get_state().click()
        self.get_state_alabama().click()
        print('Click state + click state Alabama + print State')

    def click_zip_code(self):
        self.get_zip_code().click()
        self.get_zip_code().send_keys("111111")
        print('Click zip code + print 111111')

    def click_phone(self):
        self.get_phone().click()
        self.get_phone().send_keys("1111111111")
        print('Click phone + print 1111111111')

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click button continue")


    # Methods

    def info_for_payment(self):
        with allure.step("Info for payment"):
            Logger.add_start_step(method='info_for_payment')
            self.read_payment_page_product_name()
            self.read_payment_page_product_price()
            self.read_payment_page_subtotal_price()
            self.read_total()
            self.click_email()
            self.click_first_name()
            self.click_last_name()
            self.click_company()
            self.click_address_line_1()
            self.click_address_line_2()
            self.click_city()
            self.click_state()
            self.click_zip_code()
            self.click_phone()
            # self.click_button_continue()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='info_for_payment')



