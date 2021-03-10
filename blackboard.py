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
url = "https://blackboard.utdl.edu"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)

# open local creds.txt and read the contents
# format of creds.txt:
# username (one space) password
with open("creds.txt", "r") as loginCreds:
    creds = loginCreds.read().split(" ")

# sign in
try:
    # Sign Into Blackboard
    u = driver.find_element_by_name("UserName")
    u.send_keys(creds[0])
    p = driver.find_element_by_name("Password")
    p.send_keys(creds[1])

    p.send_keys(Keys.RETURN)
    print("Login Success")
except:
    print("Login Error - Check Credentials")
    driver.quit()
    exit()

# find quiz
try:
    # wait 120 seconds to find quiz before forgoing search for quiz
    element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.ID, "saveButton_1"))
    )
    # found open quiz
    print("Quiz has been opened.")
    # counts # of questions on quiz
    count = len(driver.find_elements_by_class_name("legend-visible"))
    print(count)
    # loops through # of questions
    content = driver.find_element_by_xpath('//legend[@class="legend-visible"]').text
    print(content)
except:
    print("Failure to find quiz.")
    driver.quit()
    exit()

# check for answers
try:
    # create headless webdriver on google
    query = (content)
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
    print("Printed immediately.")
    copiedText = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.TermText"))).text
    print(copiedText)
    answer = driver.find_element_by_xpath("//span[contains(text(), 'New Moon')]/following-sibling::span")
    print(answer)
    print(copiedText)
except:
    print("error message")