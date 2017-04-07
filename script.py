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

# abre popup dos seguidores
followers_icon = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/followers/')]")
followers_icon.click()

sleep(2)

popup_followers = chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
popup_followers.click()

#carrega todos os que me seguem
for _ in range(0, 30):
    popup_followers.send_keys(Keys.PAGE_DOWN)
    popup_followers.send_keys(Keys.PAGE_DOWN)
    sleep(1)

elements_followers = chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
list_followers = map(lambda x: x.get_attribute('innerHTML'), elements_followers)

print len(list_followers)

bt_close = chrome.find_element_by_xpath("//div[@class='_quk42']")
bt_close.send_keys(Keys.ESCAPE)

following_icon = chrome.find_element_by_xpath("//a[contains(@href,'/"+username+"/following/')]")
following_icon.click()

sleep(2)

popup_following = chrome.find_element_by_xpath("//div[contains(@class,'_4gt3b')]")
popup_following.click()

# carrega todos os que sigo
for _ in range(0, 30):
    popup_following.send_keys(Keys.PAGE_DOWN)
    popup_following.send_keys(Keys.PAGE_DOWN)
    sleep(1)

elements_following = chrome.find_elements_by_xpath("//a[contains(@class,'_4zhc5')]")
list_following = map(lambda x: x.get_attribute('innerHTML'), elements_following)

for following in list_following:
    if following not in list_followers:
        print following

print len(list_following)