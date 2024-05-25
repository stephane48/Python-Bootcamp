from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")

# By.CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By.XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")

# Challenge: Print the event dates from python.org
event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for time in event_time:
#     print(time.text)
events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text
    }
print(events)

# driver.close()
driver.quit()

