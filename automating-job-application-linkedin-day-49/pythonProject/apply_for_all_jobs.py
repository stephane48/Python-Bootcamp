import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

ACCOUNT_EMAIL = "your_email"
ACCOUNT_PASSWORD = "your_password"

# Solution: https://gist.github.com/TheMuellenator/3cc1fdb5f43db6c5d1dd8f773fa4b05c

def abort_application():
    try:
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        # Click Discard Button
        discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
    except NoSuchElementException:
        pass


def handle_modal():
    try:
        # Close any blocking modals
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
    except NoSuchElementException:
        pass


# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to LinkedIn jobs search page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click on the sign-in button
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

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

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    try:
        handle_modal()
        listing.click()
        time.sleep(2)

        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        # phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except (NoSuchElementException, ElementClickInterceptedException) as e:
        abort_application()
        print(f"Exception occurred: {str(e)}. Skipped.")
        continue

time.sleep(5)
driver.quit()
