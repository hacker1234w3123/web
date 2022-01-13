from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv 

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:\DHRUV\Whitehat Projects\assignment projects\Web scrapping\chromedriver_win32\chromedriver.exe")

browser.get(url)

def scrap ():
    headers = ["Name" , "Distance" , "Mass","Radius"]
    planet_Data = []
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for i in range(0,489):
        all_tr_tag = soup.find_all("tr")
        for tr_tag in all_tr_tag:
            all_li_tag = tr_tag.find_all("td")
            templist = []
            for index,td_tag in enumerate (all_tr_tag):
                if index == 0 :
                    contents = td_tag.find_all("span")[0].contents[0]
                    templist.append(contents)
                else:
                    templist.append(td_tag.contents[0])
            planet_Data.append(templist)
        print(planet_Data)
    browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/table/tbody/tr[1]/td[1]/span[1]").click()
    

scrap()

