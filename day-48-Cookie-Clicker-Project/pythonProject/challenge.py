from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the "Search" <input> by Name
search_f_name = driver.find_element(By.NAME, value="fName")
search_l_name = driver.find_element(By.NAME, value="lName")
search_email = driver.find_element(By.NAME, value="email")

# Sending keyboard input to Selenium
search_f_name.send_keys("Stephane")
search_l_name.send_keys("Kamdem")
search_email.send_keys("stephanekamdem09@gmail.com")

# Find element by Button
sign_up_button = driver.find_element(By.TAG_NAME, value="button")
sign_up_button.click()




