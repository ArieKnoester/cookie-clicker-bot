# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")


# When the browser first opens a prompt will display asking the user for a language preference.
# However, this prompt does not display immediately. The line below forces selenium to wait
# (up to 10 secs) for the "English' button to be clickable.
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))).click()

# Once a language is selected the site will reload. We need to wait until the cookie is clickable.
# Error message:
# ElementClickInterceptedException: Message: Element <button id="bigCookie"> is not clickable
# at point (192,234) because another element <div id="loader"> obscures it
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.ID, "bigCookie")))

cookie = driver.find_element(By.ID, value="bigCookie")
while True:
    cookie.click()

    cookies_per_minute = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
    # print(cookies_per_minute)

    products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    product_prices = []
    for product in products:
        # print(product.text.replace("\n", " ").split(" ")[1])
        product_prices.append(int(product.text.replace("\n", " ").split(" ")[1]))

    if product_prices:
        print(product_prices)
        max_price_product_position = product_prices.index(max(product_prices))
        print(max_price_product_position)
        WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.ID, f"product{max_price_product_position}"))).click()
        # product_to_buy = driver.find_element(By.ID, value=f"product{max_price_product_position}")
        # print(product_to_buy.text)
        # product_to_buy.click()


# driver.quit()
