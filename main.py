import urllib.request
import bs4 as bs
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
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
    clean = re.compile('<.*?>')
    reviewBtn = driver.find_elements(by=By.CLASS_NAME, value ='btn')
    if len(reviewBtn)>=3:
        reviewBtn[2].click()

        time.sleep(3)
        for i in range(6):
            driver.current_url
            readMore = driver.find_elements(by=By.CLASS_NAME, value ='btn-block')
            if readMore:
                driver.find_elements(by=By.CLASS_NAME, value ='btn-block')[0].click()
                time.sleep(1)
            else:
                break

        html_source = driver.page_source
        soup = bs.BeautifulSoup(html_source, features="html.parser")
        comments = []
        for tag in soup.find_all('p',class_="f-500"):
            comments.append(re.sub(clean,'',str(tag)))
            # comments.append(tag)
        
        time.sleep(1)
        # driver.find_elements(by=By.XPATH,value='//a[@href="/oman/restaurants/1415"]')[0].click()
        # time.sleep(2)
        return comments
    else:
        return []


if __name__ == "__main__":
    driverPath = os.path.join("C:\\Users\\ajasu\\Downloads","chromedriver.exe")
    driver = webdriver.Chrome(executable_path=driverPath)
    for i in range(7):
        site = f'https://www.talabat.com/oman/restaurants/1415/al-mawalih-north?page={i+1}'
        driver.get(site)
        time.sleep(1)
        restButtons = driver.find_elements(by=By.CLASS_NAME, value ='restuarant-item')
        comments = []

        for i in range(len(restButtons)):
            driver.get(site)
            time.sleep(1)
            restButtons = driver.find_elements(by=By.CLASS_NAME, value ='restuarant-item')
            restButtons[i].click()
            time.sleep(3)
            temp = getRestaurantData()
            for c in temp:
                comments.append(c)

    time.sleep(1)
    s = pd.Series(comments)
    s = s.str.strip()
    path = os.path.abspath(os.path.curdir)
    s.to_csv(os.path.join(path,'comments.csv'))
    print(comments)
    driver.close()