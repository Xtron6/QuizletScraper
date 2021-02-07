# import webdrivers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# misc imports
import time

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
    # wait 60 seconds to find quiz before forgoing search for quiz
    element = WebDriverWait(driver, 60).until(
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

# chceck for answers
try:
    # create headless webdriver on google
    url = "https://www.google.com/"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url)
    # google question
    search = driver.find_element_by_name("q")
    search.send_keys(content)
    search.send_keys(Keys.RETURN)  # hit return after you enter search text
    time.sleep(3)  # sleep for 5 seconds so you can see the results
    driver.find_element_by_xpath('//*[@class="LC20lb DKV0Md"]').click()
    print("headless success")
except:
    print("failure to search google")
    driver.quit()
    exit()