from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from random import *
import csv
import os
import time

from bs4 import BeautifulSoup
import requests


############LIST OF XPATHS##############
cookie1 = "/html/body/div[1]/div/div/div/div[4]/ul/li[1]/div/label[2]"
cookie2 = "/html/body/div[1]/div/div/div/div[4]/ul/li[2]/div/label[2]"
cookiebtn = "/html/body/div[1]/div/div/div/div[5]/button"



textentry = "/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input"
slayerbtn = "/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li/div/div/div/div/div[3]/button[2]"

songnext = "/html/body/div[1]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/a"
motiveernext = "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/a/div/span[2]"

name = '//*[@id="name"]'
email = '//*[@id="email"]'

tandc = '//*[@id="accept"]'


############Name Generator##############
#The following funciton creates a random dutch name from the list of top 10000 first and last names
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

##########Email Generator###############

def getmail():
    r = requests.get("https://www.10minutemail.com", timeout=5)

    pc = BeautifulSoup(r.content, "html.parser")

    email = pc.find("input", {"id": "mailAddress"}).get('value')

    return email







############Vote Function###############
#The function below votes for the required minimum 5 songs, including ANGEL OF DEATH.
#Randomizer is used so that slayer is not always the n-th song selected to make it seem less "bot-y"

def vote():

    driver = webdriver.Firefox()
    driver.get("https://stem.nporadio2.nl/top2000/1")


    #Waittimes definition
    wtl = 1.5
    wts = 0.7

    #Focking cookies man
    cookielist = [cookie1, cookie2, cookiebtn]
    print(cookielist)
    for x in cookielist:
        time.sleep(wts)
        driver.find_element_by_xpath(x).click()


    #Voting
    position = randint(1,5)

    print("Position is " + str(position))   #Randomised position of slayer song in the list
    for x in range(1,6):
        #Vote for Slayer
        if x == position:
            #select field and search add slayer if
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(wtl)
            driver.find_element_by_xpath(textentry).send_keys("slayer")
            #maybe add a wait here in case it tries to select the add button too quickly
            time.sleep(wtl)
            driver.find_element_by_xpath(slayerbtn).click()
            time.sleep(wtl)
            driver.find_element_by_xpath(textentry).clear()
            time.sleep(wtl)

        #Vote for random song in top of list
        else:
            currentsong = "/html/body/div[1]/div/div/div[3]/div[2]/div/ul/div/div/li[%s]/div/div/div/div/div[3]/button[2]" % (str(x),)

            #if its far down the list, scroll it into view
            if x >= 3:
                driver.execute_script("window.scrollTo(0, 500)")
            #Vote for the song
            time.sleep(wts)
            driver.find_element_by_xpath(currentsong).click()
            time.sleep(wts)
            print("vote %s was cast" % (x,))

    #Song selection is now complete. We now need to fill in name/email and submit the vote

    #Click through to next pages
    time.sleep(wts)
    driver.find_element_by_xpath(songnext).click()
    time.sleep(wtl)
    driver.find_element_by_xpath(motiveernext).click()
    time.sleep(wtl)


    #Call name generator to enter a random name
    driver.find_element_by_xpath(name).send_keys(namegenerator())
    time.sleep(wts)
    driver.find_element_by_xpath(email).send_keys(getmail())
    time.sleep(wts)


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(wts)
    driver.find_element_by_xpath(tandc).click()



vote()
