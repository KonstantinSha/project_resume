import allure
import pytest
import time
from selenium import webdriver
from Project_resume.pages.account_page import Account_page
from Project_resume.pages.login_page import Login_page
from Project_resume.pages.payment_page import Payment_page
from Project_resume.pages.start_page import Start_page
from Project_resume.pages.cart_page import Cart_page
from Project_resume.pages.main_page import Main_page
from Project_resume.pages.product_page import Product_page
from selenium.webdriver.chrome.options import Options


@allure.description("Test buy product 1")
def test_buy_product_1():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:/Users/ASUS/Desktop/PythonQA/2.1/Selenium/chromedriver.exe', chrome_options=options)

    print("Start test 1")

    sp = Start_page(driver)
    sp.enter_login_page()

    lp = Login_page(driver)
    lp.authorization()

    ap = Account_page(driver)
    ap.enter_main_page()

    mp = Main_page(driver)
    mp.select_product()

    pp = Product_page(driver)
    pp.add_to_cart_product()

    cp = Cart_page(driver)
    cp.transition_to_payment()

    payp = Payment_page(driver)
    payp.info_for_payment()

    print('Finish test 1')
    time.sleep(5)
    driver.quit()



