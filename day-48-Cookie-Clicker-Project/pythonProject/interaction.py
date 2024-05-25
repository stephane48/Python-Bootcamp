from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Home in on anchor tag using CSS selectors
article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_number.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)




# driver.close()
# driver.quit()
