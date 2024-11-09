from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import io
import functions
import time


def main(link):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    driver = webdriver.Chrome()
    url = link
    driver.get(url)
    functions.closeCookiesWindow(driver)
    
    functions.foulsPlayer(driver)
    functions.playerName(driver)
    functions.matches(driver)
    functions.matchTeams(driver)
    functions.matchFouls(driver)


    
