from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (I've picked Chrome for the exercise)
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

# NUVOLAR REVIEWER PLEASE READ:

# I haven't had time to finsih it but here you have my clarified and suggested improved scenarios along with a description of how I planned on proceeding from here:
#
# Clarified and Improved Scenario Specification

# Objective: 
# Validate that the Amazon shopping cart updates and displays the correct total price and quantity when items are added and updated in the cart.

# Steps:
# 1. Navigate to the Amazon homepage (https://www.amazon.com).
# 2. Search for the term "hats for men".
# 3. Identify the first hat in the search results and add it to the Cart with a quantity of 2.
# 4. Go to the Cart and verify that the total price and quantity reflect the addition of 2 hats for men.
# 5. Return to the homepage and search for "hats for women".
# 6. Add the first hat in the search results to the Cart with a quantity of 1.
# 7. Visit the Cart again and check that the total price and quantity are updated correctly.
# 8. In the Cart, adjust the quantity for the "hats for men" from 2 to 1.
# 9. Assert that the Cart's total price and quantities reflect this change accurately.

# Improvements:
# - Specified the objective at the beginning to set context.
# - Added explicit navigation back to the homepage, to prevent ambiguity.
# - Included steps to verify cart updates, which improves readability and sets clear expectations for the outcome.

# Step 4: Open cart and assert total price and quantity are correct

# Navigating to the cart would be done here, followed by:
# - Locating the item price element
# - Locating the subtotal element
# - Locating the quantity element
# - Extracting the text and parsing to int or float
# - Asserting the expected total price and quantity

# Step 5-9: Similar steps follow, altering search terms, finding elements, and making assertions

# Please note this script is an outline. 
# I haven't addressed dynamic element IDs, waits or variations in layouts.

driver.quit()