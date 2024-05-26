import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your_email"
TWITTER_PASSWORD = "your_password"


# 1. Create a class called InternetSpeedTwitterBot
class InternetSpeedTwitterBot:
    def __init__(self):
        # 2. In the init() method, create the Selenium driver and 2 other properties down and up .
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    # 3. Create two methods - get_internet_speed() and tweet_at_provider() .
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        close_button = self.driver.find_element(By.LINK_TEXT, value="Back to test results")
        close_button.click()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                               '1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                  '1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                       '1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div['
                                                       '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div['
                                                      '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                      '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


# 4. Outside the class, initialise the object and call the two methods in order.
# Where you first get the internet speed and then tweet at the provider.
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
