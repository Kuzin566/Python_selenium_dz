import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from pages.header_page import Header_page
from pages.login_page import Login_page


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_position = ""
    product_name = ''
    product_price = ''


    #Locators:
    l_total_price = "//*[@id='allSum_FORMATED']"                    #Локатор итоговой суммы
    l_checkout_button = "//*[@class='checkout']"                    #Локатор кнопки Оформить заказ"
    l_clean_cart_button = "//span[@class = 'delete_all btn btn-default white white-bg grey remove_all_basket']"

    #Getters:
    def get_product_name(self, products_position):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,f".//tr[@class='mainrow basket_row'][{products_position}]")))

    def get_product_price(self, products_position):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, f".//tr[@class='mainrow basket_row'][{products_position}]//div[@class = 'current_price']")))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_total_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_checkout_button)))

    def get_clean_cart_button(self):
        return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, self.l_clean_cart_button)))



    #Actions:
    def text_product_name(self, product_positions):
        product_name = self.get_product_name(product_positions).get_attribute('data-item-name')
        return product_name


    def text_product_price(self, product_positions):
        product_price = self.get_product_price(product_positions).get_attribute('innerText')
        return product_price.split(' ')[0]


    def assert_product_name(self, product_positions, product_name):
        assert product_name == self.text_product_name(product_positions)
        print("Название продукта в корзине совпадает с названием из каталога : " + product_name)


    def assert_product_price(self, product_positions, product_price):
        assert product_price == self.text_product_price(product_positions)
        print("Цена продукта в корзине совпадает с ценой из каталога : " + product_price + " RUB")

    def text_total_price(self):
        total_price = self.get_total_price().get_attribute('innerText')
        return total_price.split(' ')[0]


    def assert_total_price(self, product_price):
        total_price = self.text_total_price()
        try:
            assert product_price == total_price
            print("Итоговая цена верная : " + total_price + ' RUB')
        except AssertionError:
            print("Значение Итого неверное, потому что товара нет в наличии\
                  Пожалуйста, запустите тест заново")
            self.driver.quit()



    def click_checkout_button(self):
        try:
            self.get_checkout_button().click()
            print("Нажали на кнопку Оформить заказ")
        except TimeoutException:
            print("Кнопки оформить заказ нет, потому что выбранного товара нет в наличии\
                  Пожалуйста, запустите тест заново")
            self.driver.close()

    def click_clean_cart_button(self):
        try:
            self.get_clean_cart_button().click()
            print("Очистили корзину от предыдущих заказов")
        except TimeoutException:
            print("Корзина пустая")



    #Metods
    def checking_order(self):
        with allure.step("Проверяем, что товар в корзине верный и переходим к оформлению заказа"):
            self.assert_product_name(self.product_position, self.product_name)
            self.assert_product_price(self.product_position, self.product_price)
            self.assert_total_price(self.product_price)
            self.click_checkout_button()
            Header_page(self.driver).assert_header_word("Оформление заказа")

    def clean_cart(self):
        with allure.step("Очищаем корзину от заказов"):
            Header_page(self.driver).cross_to_cart()
            self.click_clean_cart_button()
            self.driver.get(Login_page.url_authorization)
