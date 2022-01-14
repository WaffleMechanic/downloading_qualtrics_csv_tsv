# James Shelton
# This program downloads the CSV and TSV files from an account in quantrics. All you need to do is put in your username
# and password.
# Notes
# - when google updates you will need to update the driver. You can aso downgrade google. They just have to match
# - If you have a slow computer you might need to raise the time.sleep and implicit waits to a higher value
# - Sorry for the excessive comments in the code. I just left my thought process down there.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("D:\chromedriver_win32\chromedriver.exe")
PATH = 'D:\chromedriver_win32\chromedriver.exe'

username = input('Please enter a username:')
password = input('Please enter a password:')

# Using Chrome to access web
driver = webdriver.Chrome(service=service)

# Open the website
driver.get('https://www.qualtrics.com/')

# we need this so that email and password are able to be entered properly. Sometimes the website takes a second to load.
driver.implicitly_wait(20)

# Finds the login button
login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/nav/div[1]/ul/li[1]/a")
# Clicks login button
login_button.click()

# This finds the username text box and then enters the username(29)
input_pass = driver.find_element(By.XPATH, "/html/body/div[3]/span/div/div/div[1]/form[2]/div[3]/input")
input_pass.send_keys(username)

# This finds the password text box and then enters the password(29)
input_pass = driver.find_element(By.XPATH, "/html/body/div[3]/span/div/div/div[1]/form[2]/div[5]/input")
input_pass.send_keys(password)

# Finds the sign in button
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/span/div/div/div[1]/form[2]/div[7]/button[1]").click()

# we need to find a way to go down a list of projects and download them one at a time.
# i didnt think about this when I started but copying the exact XPATH is probably not going to work
# I would have to hard code every single one.... The point of writing this is so i dont have to do this lol

# Solution :D
# Step one: Find the product list. We can use Xpath here since there is only one.
# Step Two: iterate through each item on the list and download files. Hard part??
# Notes: there should be a system in place so it compares what was just downloaded to the item it is looking at.
# This should help with iterating through.

# some testing to see how to grab this element

# This is Fine and dandy but a loop would be way more efficient. Glad to know it works though :D

# This bit of code allows us to click on the very first survey. Now... How to iterate...
# test = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[1]")
# test.click()
#
# # allow the page to catch up
# driver.implicitly_wait(20)


def download_files():
    """This method downloads the CSV and TSV files"""
    # Download the files.
    # Step 1. go to data analysis.
    data_analysis_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/global-wrapper-react-header/global-wrapper-top-nav/div/nav[2]/div/ul/li[3]/a/div[1]")
    data_analysis_button.click()
    driver.implicitly_wait(20)

    # Opens drop down menu
    drop_down = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/span[2]").click()
    driver.implicitly_wait(20)

    # Clicks export
    export = driver.find_element(By.XPATH, "/html/body/div[8]/ul/li[1]").click() # I will be using this format now. looks better

    # Download CSV
    CSV = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div/div[3]/button[1]").click()
    time.sleep(10)

    # Click close
    close = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div/div[3]/button").click()

    # Opens drop down menu
    drop_down = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/span[2]").click()

    # Clicks export
    export = driver.find_element(By.XPATH, "/html/body/div[8]/ul/li[1]").click() # I will be using this format now. looks better

    # Move to and Download TSV
    TSV_button = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div/div[2]/div/div[1]/div/div[2]").click()
    TSV = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div/div[3]/button[1]").click()
    time.sleep(10)

    # closes the download page
    close = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div/div[3]/button").click()

    # goes back to the project list.
    driver.back()

# Functionalities that are still needed.
# 1. Download files
# 2. Check to see if there are any more surveys.

# if testing to see if there are any more items to be downloaded is tough just ask the user how many surveys they
# would like to download. Then iterate through that number.

# Change this number if you want to start on a different survey. Ex. num = 17 starts on the 17th survey.
num = 1

# Iterates through each project
while True:
    try:
        # finds and clicks a survey button.
        item = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[{num}]")
        item.click()

        # increases num by one, so we will click on the next survey
        num += 1
        # debug
        # print(num)

        # We need to actually download the files right here. There will be a nested loop.
        download_files()

        # After files are downloaded we go back to projects page.
        driver.back()

        # debug
        # print(num)

    except:
        print("All downloads have been completed. Please double check the files!")
        break

