from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
#====================================================================================================================================================================================================================

def getColor(driver, last):
    color=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[3]/ul/li[1]")
    number = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[4]/div[1]/span/span")
    color=color.get_attribute('class')
    number = int(number.text)
    if number==last[0]+1:
        i = 0
        while not color[i] == ' ':
            i+=1
        color=color[i+1:]
        round=color
        last[0]=number
        return round
    else:
        return 0
def getNumberOfFirstGame(driver):
    number=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[4]/div[1]/span/span")
    #print(int(number.text))
    return int(number.text)

#====================================================================================================================================================================================================================

driver=webdriver.PhantomJS()
driver.set_window_size(1920,1080)
driver.get('http://csgofast.com/#game/double')
last=[getNumberOfFirstGame(driver)]



while 1:
   if last[0]+1 == getNumberOfFirstGame(driver):
       print(getColor(driver,last))



driver.quit()

