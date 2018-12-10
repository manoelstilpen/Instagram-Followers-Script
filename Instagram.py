#coding: utf-8

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Instagram:

    def __init__(self, username=None, passw=None):
        self.__username = username
        self.__password = passw
        self.__nfollowers = 0
        self.__nfollowing = 0
        self.__list_followers = []
        self.__list_following = []
        self.__non_followers = []
        self.__chrome = webdriver.Firefox()
        self.__chrome.wait = WebDriverWait(self.__chrome, 5)
        self.__chrome.get("http://instagram.com")
        self.__chrome.implicitly_wait(10)
        assert "Instagram" in self.__chrome.title

        # log with an existent account
        self.__chrome.wait.until(EC.presence_of_element_located((By.LINK_TEXT, u'Log in'))).click()

        name = self.__chrome.find_element_by_name("username")
        passw = self.__chrome.find_element_by_name("password")

        if self.__username is not None and self.__password is not None:
            # enter username and password
            name.send_keys(self.__username)
            passw.send_keys(self.__password)
        else:
            print "User is not defined"

        # enter key is pressed to log in
        passw.send_keys(Keys.RETURN)
        # wait to load the page
        sleep(3)

    def open_profile(self):

        if self.__chrome.find_element_by_xpath("//div[contains(@class, 'piCib')]") is not None: # clicar em nao exibir notificacoes
            self.__chrome.find_element_by_xpath("//button[contains(@class, 'HoLwm')]").click()


        self.__chrome.find_element_by_xpath("//a[contains(@class,'coreSpriteDesktopNavProfile')]").click() # clicar no link para abrir perfil
        sleep(2)

        self.__nfollowers = int(self.__chrome.find_element_by_xpath("//a[contains(@href,'/" + self.__username + "/followers/')]/span[@class='g47SY ']").get_attribute('innerHTML'))
        self.__nfollowing = int(self.__chrome.find_element_by_xpath("//a[contains(@href,'/" + self.__username + "/following/')]/span[@class='g47SY ']").get_attribute('innerHTML'))

    def get_followers(self):

        # abre popup dos seguidores
        self.__chrome.find_element_by_xpath("//a[contains(@href,'/"+self.__username+"/followers/')]").click()

        popup_followers = self.__chrome.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'isgrP')]")))
        popup_followers.click()
        sleep(2)
        followers_lenght = 0
        while followers_lenght < self.__nfollowers:
#            popup_followers.send_keys(Keys.PAGE_DOWN)
            popup_followers.send_keys(Keys.PAGE_DOWN)
            followers_lenght = len(map(lambda x: x.get_attribute('innerHTML'),
                self.__chrome.find_elements_by_xpath("//a[contains(@class,'FPmhX')]")))
            print (str(followers_lenght) + " " + str(self.__nfollowers))
            sleep(0.5)
        elements_followers = self.__chrome.find_elements_by_xpath("//a[contains(@class,'FPmhX')]")
        self.__list_followers = map(lambda x: x.get_attribute('innerHTML'), elements_followers)

        # testa se leu todos os seguidores
        assert len(self.__list_followers) == self.__nfollowers, 'Failed loading all followers'

        # close pop up followers        
        self.__chrome.find_element_by_xpath("//div[contains(@class, 'pbNvD')]//button[contains(@class,'dCJp8')]").click() # clica no X do popup

    def get_following(self):

        # abre pop-up das pessoas que segue
        self.__chrome.find_element_by_xpath("//a[contains(@href,'/"+self.__username+"/following/')]").click()

        popup_following = self.__chrome.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'isgrP')]")))
        popup_following.click()

        following_lenght = 0
        while following_lenght < self.__nfollowing:
#            popup_following.send_keys(Keys.PAGE_DOWN)
            popup_following.send_keys(Keys.PAGE_DOWN)
            following_lenght = len(map(lambda x: x.get_attribute('innerHTML'),
                                       self.__chrome.find_elements_by_xpath("//a[contains(@class,'FPmhX')]")))
            print (str(following_lenght) + " " + str(self.__nfollowing))
            sleep(0.5)

        elements_following = self.__chrome.find_elements_by_xpath("//a[contains(@class,'FPmhX')]")
        self.__list_following = map(lambda x: x.get_attribute('innerHTML'), elements_following)

        assert len(self.__list_following) == self.__nfollowing, "Failed loading all following"

        # close pop up followers        
        self.__chrome.find_element_by_xpath("//div[contains(@class, 'pbNvD')]//button[contains(@class,'dCJp8')]").click() # clica no X do popup
#        popup_following.send_keys(Keys.ESCAPE)

    def get_non_followers(self):
        self.open_profile()
        self.get_followers()
        self.get_following()

        self.__chrome.close()

        print "PEOPLE WHO DONT FOLLOW YOU BACK:"
        for following in self.__list_following:
            if following not in self.__list_followers:
                print following
                self.__non_followers.append(following)


