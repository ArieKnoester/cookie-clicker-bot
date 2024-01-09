# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from datetime import datetime, timedelta
import time

SITE_URL = "https://orteil.dashnet.org/cookieclicker/"
PRODUCT_CHECK_INTERVAL = timedelta(seconds=5)


def check_products(*, web_driver, cookie_count):
    # debugging
    # print('check products executed @', time.asctime())
    # print(current_cookie_count)

    available_products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    product_names = []
    # product_prices = []
    for product in available_products:
        # print(product.text.replace("\n", " ").split(" ")[1])
        # product_prices.append(int(product.text.replace("\n", " ").split(" ")[0]))
        product_names.append(product.text.replace("\n", " ").split(" ")[0])

    if product_names:
        # print(product_names)

        highest_tier_product_available = len(product_names) - 1
        product_to_buy = driver.find_element(By.ID, value=f"product{highest_tier_product_available}")
        # print(product_to_buy.text)
        product_to_buy.click()


def prepare_site(web_driver):

    # Wait 2 secs, otherwise a <p class="cc_message">
    # will obscure the accept cookies button
    time.sleep(2)

    # We need to click the accept cookies button, otherwise this bot will
    # not be able to click on products in the 'Buildings' panel.
    WebDriverWait(web_driver, timeout=10).until(
        element_to_be_clickable((By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all"))).click()

    # A prompt will display asking the user for a language preference.
    WebDriverWait(web_driver, timeout=10).until(element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))).click()

    # Once a language is selected the site will reload. We need to wait until the cookie is clickable.
    # Error message:
    # ElementClickInterceptedException: Message: Element <button id="bigCookie"> is not clickable
    # at point (192,234) because another element <div id="loader"> obscures it
    WebDriverWait(web_driver, timeout=10).until(element_to_be_clickable((By.ID, "bigCookie")))


driver = webdriver.Firefox()
driver.get(SITE_URL)
prepare_site(driver)

cookie = driver.find_element(By.ID, value="bigCookie")
timeout = time.time() + (60 * 5)  # 60 sec * 5 =  5 minutes
last_time_products_checked = datetime.now()

while time.time() < timeout:
    cookie.click()
    current_cookie_count = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])

    if last_time_products_checked <= (datetime.now() - PRODUCT_CHECK_INTERVAL):
        check_products(web_driver=driver, cookie_count=current_cookie_count)
        last_time_products_checked = datetime.now()

cookies_per_second = driver.find_element(By.ID, value="cookiesPerSecond")
print(cookies_per_second.text)
driver.quit()
