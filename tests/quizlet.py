# import webdrivers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# misc imports
import time

#import Google scrape (lxml)

# set url and paths
DRIVER_PATH = "drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
try:
    # create headless webdriver on google
    query = ("Phases of the Moon Flashcards | Quizlet")
    query = query.replace(' ', '+')
    url = f"https://google.com/search?q={query}"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url)
    # google question
    driver.find_element_by_partial_link_text("Quizlet").click()
    print("Close matching Quizlet found.")
except:
    print("failure to search google")
    driver.quit()
    exit()
try:   
    print("There is no Facebook account to sign in to.")
    driver.find_element_by_xpath("//span[contains(text(), 'New Moon')]").click()
    answer = driver.find_element_by_xpath("//span[contains(text(), 'New Moon')]")
    print("Printed immediately.")
    print(answer)
except:
    print("error message")
    