import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = sys.argv[1]
password = sys.argv[2]

chrome = webdriver.Firefox()
chrome.get("http://instagram.com")
assert "Instagram" in chrome.title

sleep(2)

logar = chrome.find_element_by_xpath("//a[@class='_fcn8k']")
logar.click()

name = chrome.find_element_by_name("username")
passw = chrome.find_element_by_name("password")

name.send_keys(username)
passw.send_keys(password)

passw.send_keys(Keys.RETURN)

sleep(3) # wait to load the page

perfil = chrome.find_element_by_xpath("//a[contains(@class,'coreSpriteDesktopNavProfile')]")
perfil.click()

sleep(2)

nfollowers = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/followers/')]/span[@class='_bkw5z']").get_attribute('innerHTML')
nfollowing = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/following/')]/span[@class='_bkw5z']").get_attribute('innerHTML')

# abre popup dos seguidores
followers_icon = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/followers/')]")
followers_icon.click()

sleep(2)

popup_followers = chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
popup_followers.click()

#carrega todos os que me seguem
for i in range(10, int(nfollowers), 10):
    popup_followers.send_keys(Keys.PAGE_DOWN)
    popup_followers.send_keys(Keys.PAGE_DOWN)
    sleep(1)

elements_followers = chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
list_followers = map(lambda x: x.get_attribute('innerHTML'), elements_followers)

assert len(list_followers) == int(nfollowers)

bt_close = chrome.find_element_by_xpath("//div[@class='_quk42']")
bt_close.send_keys(Keys.ESCAPE)

following_icon = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/following/')]")
following_icon.click()

sleep(2)

popup_following = chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
popup_following.click()

# carrega todos os que sigo
for i in range(10, int(nfollowing), 10):
    popup_following.send_keys(Keys.PAGE_DOWN)
    popup_following.send_keys(Keys.PAGE_DOWN)
    sleep(1)

elements_following = chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
list_following = map(lambda x: x.get_attribute('innerHTML'), elements_following)

assert len(list_following) == int(nfollowing)

non_followers = []
for following in list_following:
    if following not in list_followers:
        non_followers.append(following)

print non_followers