from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://instagram.com")
assert "Instagram" in driver.title

elem = driver.find_element_by_class_name("_fcn8k")
elem.click()
elem = driver.find_element_by_name("username")
elem.send_keys("manoelstilpen")
elem = driver.find_element_by_name("password")
elem.send_keys("")
elem.send_keys(Keys.RETURN)

<a class="_soakw _vbtk2 coreSpriteDesktopNavProfile" href="/manoelstilpen/">Perfil</a>
# //*[@id="react-root"]/section/nav/div/div/div/div[3]/div/div[3]/a
# elem = driver.find_element_by_xpath("//section/nav/div/div/div/div[3]/div/div[3]/a")
elem = driver.find_element_by_tag_name("")
elem.click()
