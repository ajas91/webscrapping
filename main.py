import urllib.request
import bs4 as bs
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os


# url = 'https://www.talabat.com/oman/restaurants/1415/al-mawalih-north'
# hdr = {'User-Agent':'Mozilla/5.0'}
# req = urllib.request.Request(url,headers=hdr)
# sauce = urllib.request.urlopen(req).read()
# soup = bs.BeautifulSoup(sauce,'html.parser') #Beautiful Soup object

# btnGroup = soup.find_all('a',class_="restuarant-item")
# for btn in btnGroup:
#     print(f'##### {btn}')


def getRestaurantData():
    reviewBtn = driver.find_elements(by=By.CLASS_NAME, value ='btn')
    reviewBtn[2].click()

    time.sleep(2)
    for i in range(4):
        driver.current_url
        readMore = driver.find_elements(by=By.CLASS_NAME, value ='btn-block')
        if readMore:
            driver.find_elements(by=By.CLASS_NAME, value ='btn-block')[0].click()
            time.sleep(2)
        else:
            break

    html_source = driver.page_source
    soup = bs.BeautifulSoup(html_source, features="html.parser")
    comments = []
    for tag in soup.find_all('p',class_="f-500"):
        comments.append(tag)
    
    time.sleep(2)
    # driver.find_elements(by=By.XPATH,value='//a[@href="/oman/restaurants/1415"]')[0].click()
    # time.sleep(2)
    return comments


if __name__ == "__main__":
    driverPath = os.path.join("C:\\Users\\ajasu\\Downloads","chromedriver.exe")
    driver = webdriver.Chrome(executable_path=driverPath)
    site = 'https://www.talabat.com/oman/restaurants/1415/al-mawalih-north'
    driver.get(site)
    time.sleep(2)
    restButtons = driver.find_elements(by=By.CLASS_NAME, value ='restuarant-item')
    comments = []

    for i in range(len(restButtons)):
        driver.get(site)
        time.sleep(2)
        restButtons = driver.find_elements(by=By.CLASS_NAME, value ='restuarant-item')
        restButtons[i].click()
        time.sleep(2)
        temp = getRestaurantData()
        for c in temp:
            comments.append(c)

    time.sleep(2)
    print(comments)
    driver.close()
