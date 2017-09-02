from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.PhantomJS()
driver.set_window_size(1920,1080)
driver.get('http://csgofast.com/#game/double')
def getColor(driver):
    color=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[3]/ul/li[1]")
    number = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[4]/div[1]/span/span")
    print(color.get_attribute('class'))
    print(color.text)
    print(int(number.text))
    return 0

def getNumberOfFirstGame(driver):
    number=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div/div[4]/div[4]/div[1]/span/span")
    print(int(number.text))
    return 0

#first=int(getNumberOfFirstGame(driver))
getColor(driver)



driver.quit()

