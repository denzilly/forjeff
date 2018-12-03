from selenium import webdriver
from random import *






##open browser and initialise browser
def initialise():

    driver = webdriver.Firefox()
    driver.get("https://stem.nporadio2.nl/top2000/1")








#The function below votes for the required minimum 5 songs, including ANGEL OF DEATH.
#Randomizer is used so that slayer is not always the n-th song selected to make it seem less "bot-y"

def vote():

    position = randint(1,5)
    for x in range(1,5):
        if x == position:
            #select field and search add slayer if
            driver.findElement(By.xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input")).sendkeys("slayer")
            #maybe add a wait here in case it tries to select the add button too quickly
            driver.findElement(By.xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/ul/div/div/li/div/div/div/div/div[3]/button[2]")).click()

        else:
            iconpath = "/html/body/div[2]/div/div/div[3]/div[2]/div/ul/div/div/li[" + str(x) + "]/div/div/div/div/div[3]/button[2]"
            driver.findElement(By.xpath(iconpath)).click()

    #click through to next pages
    driver.findElement(By.xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/a")).click()
    #wait?
    driver.findElement(By.xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/a")).click()


def personalinfo():



initialise()
