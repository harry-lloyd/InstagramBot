from selenium import webdriver
from time import sleep
from secrets import password


class InstaBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(4)

    # Login and click through pop-ups
    def login(self, username, password):
        self.username = username
        self.password = password
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/button[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')\
            .send_keys(password)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        sleep(1)

    # Like the users most recent post
    def like_recent(self, account_name):
        self.driver.get("https://instagram.com/" + account_name + "/")
        sleep(5)
        self.driver.find_element_by_class_name('v1Nh3.kIKUG._bz0w').click()
        sleep(3)
        self.driver.find_element_by_class_name('fr66n').click()


# Store class in a variable and call the login function to... login.
instabot = InstaBot()
instabot.login("harry9lloyd", password)

# Add users account name here
instabot.like_recent("therock")
