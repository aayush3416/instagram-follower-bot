from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "YOUR OWN CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "THE ACCOUNTS FOLLOWERS YOU WANT TO FOLLOW"
USERNAME = "YOUR OWN USERNAME "
PASSWORD = "YOUR OWN PASSWORD"


class InstagramFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[1]/div/div[3]/button')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            if button.text != "Follow":
                pass
            else:
                button.click()
                time.sleep(2)


bot = InstagramFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()



