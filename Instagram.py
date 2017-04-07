from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Instagram:

    def __init__(self, username=None, passw=None):
        self.username = username
        self.password = passw
        self.nfollowers = 0
        self.nfollowing = 0
        self.list_followers = []
        self.list_following = []
        self.non_followers = []
        self.chrome = webdriver.Firefox()
        self.chrome.get("http://instagram.com")
        assert "Instagram" in self.chrome.title

        sleep(2)

        # log with an existent account
        self.chrome.find_element_by_xpath("//a[@class='_fcn8k']").click()

        name = self.chrome.find_element_by_name("username")
        passw = self.chrome.find_element_by_name("password")

        if username is not None and self.password is not None:
            # enter username and password
            name.send_keys(self.username)
            passw.send_keys(self.password)
        else:
            print "User is not defined"

        # enter key is pressed to log in
        passw.send_keys(Keys.RETURN)
        # wait to load the page
        sleep(3)

    def open_profile(self):
        self.chrome.find_element_by_xpath("//a[contains(@class,'coreSpriteDesktopNavProfile')]").click()
        sleep(2)

        self.nfollowers = self.chrome.find_element_by_xpath("//a[contains(@href,'/" + self.username + "/followers/')]/span[@class='_bkw5z']").get_attribute('innerHTML')
        self.nfollowing = self.chrome.find_element_by_xpath("//a[contains(@href,'/" + self.username + "/following/')]/span[@class='_bkw5z']").get_attribute('innerHTML')

    def get_followers(self):

        # abre popup dos seguidores
        followers_icon = self.chrome.find_element_by_xpath("//a[contains(@href,'/"+self.username+"/followers/')]")
        followers_icon.click()

        sleep(2)

        popup_followers = self.chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
        popup_followers.click()

        #carrega todos os que me seguem
        for _ in range(10, int(self.nfollowers), 10):
            popup_followers.send_keys(Keys.PAGE_DOWN)
            popup_followers.send_keys(Keys.PAGE_DOWN)
            sleep(1)

        elements_followers = self.chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
        self.list_followers = map(lambda x: x.get_attribute('innerHTML'), elements_followers)

        # testa se leu todos os seguidores
        assert len(self.list_followers) == int(self.nfollowers), "Failed loading all followers"

        self.chrome.find_element_by_xpath("//div[@class='_quk42']").send_keys(Keys.ESCAPE)

    def get_following(self):
        following_icon = self.chrome.find_element_by_xpath("//a[contains(@href,'/"+self.username+"/following/')]")
        following_icon.click()

        sleep(2)

        popup_following = self.chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
        popup_following.click()

        # carrega todos os que sigo
        for _ in range(10, int(self.nfollowing), 10):
            popup_following.send_keys(Keys.PAGE_DOWN)
            popup_following.send_keys(Keys.PAGE_DOWN)
            sleep(1)

        elements_following = self.chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
        self.list_following = map(lambda x: x.get_attribute('innerHTML'), elements_following)

        assert len(self.list_following) == int(self.nfollowing), "Failed load all following"

        self.chrome.find_element_by_xpath("//div[@class='_quk42']").send_keys(Keys.ESCAPE)

    def get_non_followers(self):
        self.open_profile()
        self.get_followers()
        self.get_following()

        print "PEOPLE WHO DONT FOLLOW YOU BACK:"
        for following in self.list_following:
            if following not in self.list_followers:
                print following
                self.non_followers.append(following)


