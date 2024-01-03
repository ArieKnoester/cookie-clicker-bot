# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# When the browser first opens a prompt will display asking the user for a language preference.
# However, this prompt does not display immediately. The line below forces selenium to wait
# (up to 10 secs) for the "English' button to be clickable.
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))).click()

# We also need to wait until the cookie is clickable. Error message:
# ElementClickInterceptedException: Message: Element <button id="bigCookie"> is not clickable
# at point (192,234) because another element <div id="loader"> obscures it
WebDriverWait(driver, timeout=10).until(element_to_be_clickable((By.ID, "bigCookie")))

driver.quit()
