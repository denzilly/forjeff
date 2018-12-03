from selenium import webdriver
from random import *
import csv
import os
import time
from selenium.webdriver.common.action_chains import ActionChains


############LIST OF XPATHS##############
cookie1 = "/html/body/div[1]/div/div/div/div[4]/ul/li[1]/div/label[2]"
cookie2 = "/html/body/div[1]/div/div/div/div[4]/ul/li[2]/div/label[2]"
cookiebtn = "/html/body/div[1]/div/div/div/div[5]/button"



textentry = "/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input"
slayerbtn = "/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li/div/div/div/div/div[3]/button[2]"

songnext = "/html/body/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/a"
motiveernext = "/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/a"







#The function below votes for the required minimum 5 songs, including ANGEL OF DEATH.
#Randomizer is used so that slayer is not always the n-th song selected to make it seem less "bot-y"

def vote():


    driver = webdriver.Firefox()
    driver.get("https://stem.nporadio2.nl/top2000/1")



    wtl = 3
    wts = 0.7
    #waittime

    #focking cookies Man

    cookielist = [cookie1, cookie2, cookie3]
    for x in cookielist:
        time.sleep(wts)
        driver.find_element_by_xpath(x).click()


    #scroll all elements into view
    lastsong = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li[6]/div/div/div/div/div[2]/p[1]")



    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView();", lastsong)


    position = randint(1,5)
    #position = 1
    print("Position is " + str(position))
    for x in range(1,5):
        if x == position:
            #select field and search add slayer if
            time.sleep(wtl)
            driver.find_element_by_xpath(textentry).send_keys("slayer")
            #maybe add a wait here in case it tries to select the add button too quickly
            time.sleep(wtl)
            driver.find_element_by_xpath(slayerbtn).click()
            time.sleep(wtl)
            driver.find_element_by_xpath(textentry).clear()


        else:
            time.sleep(wts)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li[%s]/div/div/div/div/div[3]/button[2]" % (str(x),)).click()
            time.sleep(wts)
            print("vote %s was cast" % (x,))

    #click through to next pages
    driver.find_element_by_xpath(songnext).click()
    time.sleep(wts)
    driver.find_element_by_xpath(motiveernext).click()


def namegenerator():

    #some junk in case working directories get messed up
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    firstnum = randint(1,9500)
    lastnum = randint(1,9500)
    def nameget(index, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row[0] for idx, row in enumerate(csv_reader) if idx in(index, index)]

            return rows

    full_name = nameget(firstnum,'voornamen.csv')[0] + " " + nameget(lastnum,'achternamen.csv')[0]

    return full_name

#print(namegenerator())

vote()
