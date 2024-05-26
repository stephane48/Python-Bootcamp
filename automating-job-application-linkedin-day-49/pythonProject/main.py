import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL = "sessegnon.stephane48@gmail.com"
ACCOUNT_PASSWORD = "Fermer48*"

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3924719384&f_AL=true&f_WT=2&geoId=101174742&keywords=python%20developer&location=Canada&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Click on the sign-in button
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Wait for the sign-in page to load
# time.sleep(2)

# Enter email and password
time.sleep(2)
search_email = driver.find_element(By.ID, value="username")
search_password = driver.find_element(By.ID, value="password")

# Sending keyword input to selenium
search_email.send_keys(ACCOUNT_EMAIL)
search_password.send_keys(ACCOUNT_PASSWORD)

# Sign-in
sign_in = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
sign_in.click()

# easy apply button
time.sleep(2)
easy_apply_button = driver.find_element(By.ID, value="ember46")
easy_apply_button.click()

# Next  button
time.sleep(2)
next_button_1 = driver.find_element(By.CSS_SELECTOR, value=".display-flex button")
next_button_1.click()

# Review button
time.sleep(2)
for review_button in driver.find_elements(By.CSS_SELECTOR, ".artdeco-button--primary"):
    if "Review" in review_button.text:
        review_button.click()
        break

# Submit Application
for submit_button in driver.find_elements(By.CSS_SELECTOR, ".artdeco-button--primary"):
    if "Submit application" in submit_button.text:
        submit_button.click()
        break






