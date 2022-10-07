from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Project_resume.base.base_class import Base
from Project_resume.utilities.logger import Logger
import allure


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    pp_product_name = "//*[@id='product-8400941969']/div/div/div[4]/div[1]/h1"
    pp_product_price = "//*[@id='product-8400941969']/div/div/div[4]/div[1]/div[2]/span[4]"
    button_colour = "//*[@id='product-8400941969']/div/div/div[4]/form/div[1]/div/div"
    button_colour_black = "//*[@id='product-select-8400941969-option-0']/option[2]"
    button_add_to_cart = "//*[@id='product-8400941969']/div/div/div[4]/form/div[2]/button[1]"
    button_go_to_cart = "//*[@id='product-8400941969']/div/div/div[4]/form/div[2]/div[2]/a[2]"


    # Getters

    def get_pp_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.pp_product_name)))


    def get_pp_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.pp_product_price)))

    def get_button_colour(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_colour)))

    def get_button_colour_black(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_colour_black)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))


    # Actions

    def read_pp_product_name(self):
        value_pp_product_name = self.get_pp_product_name().text
        print(value_pp_product_name)

    def read_pp_product_price(self):
        value_pp_product_price = self.get_pp_product_price().text
        print(value_pp_product_price)

    def click_button_colour(self):
        self.get_button_colour().click()
        print('Click button colour')

    def click_button_colour_black(self):
        self.get_button_colour_black().click()
        print('Click button colour black')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('Click button add to cart')

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print('Click button go to cart')


    # Methods

    def add_to_cart_product(self):
        with allure.step("Add to cart product"):
            Logger.add_start_step(method='add_to_cart_product')
            self.read_pp_product_name()
            self.read_pp_product_price()
            self.click_button_colour()
            self.click_button_colour_black()
            self.click_button_add_to_cart()
            self.click_button_go_to_cart()
            self.assert_url("https://www.maxpedition.com/cart")
            Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_product')


