from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (assuming Chrome)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Step 1: Go to Amazon
driver.get("https://www.amazon.com")

# Step 2: Search for "hats for men"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("hats for men")
search_box.send_keys(Keys.RETURN)

# Step 3: Add first hat to Cart with quantity 2
first_hat = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']:first-child"))
)
first_hat.click()

add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "add-to-cart-button"))
)
add_to_cart_button.click()

# If quantity selection is present, set to 2; otherwise, add the item again
try:
    quantity_dropdown = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "quantity"))
    )
    quantity_dropdown.send_keys('2')
    quantity_dropdown.send_keys(Keys.RETURN)
except Exception:
    add_to_cart_button.click()

# Step 4: Open cart and assert total price and quantity are correct

# Navigating to the cart would be done here, followed by:
# - Locating the item price element
# - Locating the subtotal element
# - Locating the quantity element
# - Extracting the text and parsing to int or float
# - Asserting the expected total price and quantity

# Step 5-9: Similar steps follow, altering search terms, finding elements, and making assertions

# Please note this script is an outline. You will need to address potential pop-ups, dynamic element IDs,
# and variation in layouts. Additionally, ensure proper waits and exception handling are in use.

# Teardown
driver.quit()