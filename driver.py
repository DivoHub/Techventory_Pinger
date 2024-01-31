from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# User-inputted query
user_query = input("Enter your search query: ")

# Set up the Chrome webdriver
chrome_options = Options()
chrome_options.headless = False  # Set to True if you don't want the browser window to appear
chrome_service = ChromeService(executable_path="/path/to/chromedriver")  # Specify the path to your chromedriver executable
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open Bing
driver.get("https://www.bing.com")

# Find and click on the shopping category
shopping_tab = driver.find_element(By.XPATH, "//a[@id='ms_nav_shop']")
shopping_tab.click()

# Find the search input and enter the user's query
search_input = driver.find_element(By.XPATH, "//input[@name='q']")
search_input.send_keys(user_query)
search_input.send_keys(Keys.RETURN)

# Wait for the results to load
driver.implicitly_wait(5)  # You may need to adjust the wait time based on your internet speed

# Get the first 20 results
results = driver.find_elements(By.XPATH, "//div[@class='product-card']")[:20]

# Print the results
for i, result in enumerate(results, start=1):
    print(f"{i}. {result.text}")

# Close the browser
driver.quit()