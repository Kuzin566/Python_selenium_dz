
import time
import allure
from pages.cart_page import Cart_page
from pages.header_page import Header_page
from pages.login_page import Login_page
from pages.order_page import Order_page
from pages.select_product_page import Select_product_page


@allure.description("")
def test_smoke_test(driver):
    lp = Login_page(driver)
    lp.autorization()                 #Авторизовываемся
    # lp.autorization_for_cookies()   #Можно авторизоваться через куки

    cp = Cart_page(driver)
    cp.clean_cart()                                #Проверяем, что корзина пустая, если корзина не пустая, то очищаем корзину

    hp = Header_page(driver)
    hp.cross_to_accumulators()                     #Переходим в Каталог/Аккумуляторы

    spp = Select_product_page(driver)              #Выбираем заказ
    spp.select_product()

    hp.cross_to_cart()

    cp.product_position = spp.product_position
    cp.product_name = spp.product_name
    cp.product_price = spp.product_price
    cp.checking_order()                             #Проверяем заказ в корзине

    op = Order_page(driver)
    op.total_price = spp.product_price
    op.order_description = 'Алекс Смит - самый крутой'
    op.registration_order()                #Проверяем информацию о заказе и оформляем заказ






