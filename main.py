# https://www.selenium.dev/documentation/
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, invisibility_of_element
from datetime import datetime, timedelta
import time

SITE_URL = "https://orteil.dashnet.org/cookieclicker/"
PRODUCT_CHECK_INTERVAL = timedelta(seconds=5)


def check_products(*, dr, cookie_count):
    print('check products executed @', time.asctime())


driver = webdriver.Firefox()
driver.get(SITE_URL)

# Wait 2 secs, otherwise a <p class="cc_message">
# will obscure the accept cookies button
time.sleep(2)

# We need to click the accept cookies button, otherwise this bot will
# not be able to click on products in the 'Buildings' panel.
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all"))).click()

# A prompt will display asking the user for a language preference.
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))).click()

# Once a language is selected the site will reload. We need to wait until the cookie is clickable.
# Error message:
# ElementClickInterceptedException: Message: Element <button id="bigCookie"> is not clickable
# at point (192,234) because another element <div id="loader"> obscures it
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.ID, "bigCookie")))

cookie = driver.find_element(By.ID, value="bigCookie")
timeout = time.time() + (60 * 5)  # 60 sec * 5 =  5 minutes
last_time_products_checked = datetime.now()

while time.time() < timeout:
    cookie.click()
    current_cookie_count = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])

    if last_time_products_checked <= (datetime.now() - PRODUCT_CHECK_INTERVAL):
        check_products(dr=driver, cookie_count=current_cookie_count)
        last_time_products_checked = datetime.now()

    # print(current_cookie_count)

    # available_products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    # product_prices = []
    # for product in available_products:
    #     # print(product.text.replace("\n", " ").split(" ")[1])
    #     product_prices.append(int(product.text.replace("\n", " ").split(" ")[1]))
    #
    # if product_prices:
    #     print(product_prices)
    #     max_price = max(product_prices)
    #     if max_price <= current_cookie_count:
    #         max_price_product_position = product_prices.index(max_price)
    #         print(f"current_cookie_count: {current_cookie_count}, max_price: {max_price}")
    #     else:
    #         product_prices.pop(max_price)
        # WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.ID, f"product{max_price_product_position}"))).click()
        # product_to_buy = driver.find_element(By.ID, value=f"product{max_price_product_position}")
        # print(product_to_buy.text)
        # product_to_buy.click()


# driver.quit()
