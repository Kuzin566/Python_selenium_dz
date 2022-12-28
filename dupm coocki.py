
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle


from pages.login_page import Login_page

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="D:\\Adminka\\selenium\\chromedriver\\chromedriver.exe" , chrome_options=options)

lp = Login_page(driver)
lp.autorization()                               #Авторизовываемся
pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
driver.close()
driver = webdriver.Chrome(executable_path="D:\\Adminka\\selenium\\chromedriver\\chromedriver.exe", chrome_options=options)
cookies = pickle.load(open("cookies.pkl","rb"))
print(cookies)
driver.get('http://adm.st.leads.tech/site/login/')
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()



