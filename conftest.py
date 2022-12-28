import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import path_driver


@pytest.fixture(autouse=True)
def set_up():
    print("\nStart test")
    yield
    print("Finish test")


@pytest.fixture()
def driver():
    options = Options()
    options.headless = False
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=path_driver, chrome_options=options)
    return driver
# D:\Adminka\selenium\chromedriver\chromedriver.exe


@pytest.fixture(scope="module")   #module действует на весь модуль, Class на весь класс и  function на всю функцию
def set_group():            #предусловие для функций в которые мы вставим эти функции
    print("Enter system")
    yield #команды которые буду выполняться после выполнения теста
    print("Exit system")

# @pytest.mark.run(order=1) задаем очередность


