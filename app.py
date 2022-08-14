from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def init_driver():
    chrome_options = Options()

    arguments = ['--window-size=1600,900', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), 
        options=chrome_options)
    return driver

driver = init_driver()

driver.get('https://www.saucedemo.com')
sleep(3)

username = 'standard_user'
password = 'secret_sauce'

username_field = driver.find_element(By.ID, 'user-name')
sleep(1)
username_field.click()
sleep(2)
username_field.send_keys(username)

password_field = driver.find_element(By.ID, 'password')
sleep(1)
password_field.click()
sleep(2)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, 'login-button')
sleep(1)
login_button.click()
sleep(3)

ordering = driver.find_element(By.CLASS_NAME, 'product_sort_container')
sleep(2)
order_by = Select(ordering)
sleep(3)
order_by.select_by_value('lohi')
sleep(1)

add_sauce_labs_onesie = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
sleep(3)
add_sauce_labs_onesie.click()
sleep(1)

add_all_the_things_tshirt_red = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
sleep(3)
add_all_the_things_tshirt_red.click()
sleep(1)

shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
sleep(3)
shopping_cart.click()
sleep(1)

checkout = driver.find_element(By.ID, 'checkout')
sleep(3)
checkout.click()
sleep(1)

first_name = driver.find_element(By.ID, 'first-name')
first_name.click()
sleep(3)
first_name.send_keys('SenseData')
sleep(1)

last_name = driver.find_element(By.ID, 'last-name')
last_name.click()
sleep(3)
last_name.send_keys('Zenvia Company')
sleep(1)

postal_code = driver.find_element(By.ID, 'postal-code')
postal_code.click()
sleep(3)
postal_code.send_keys('05435-011')
sleep(1)

continue_button = driver.find_element(By.ID, 'continue')
sleep(3)
continue_button.click()
sleep(3)

driver.execute_script('window.scrollTo(0, 300);')
finish = driver.find_element(By.ID, 'finish')
sleep(3)
finish.click()
driver.execute_script('window.scrollTo(0, -200);')
sleep(10)

driver.close()