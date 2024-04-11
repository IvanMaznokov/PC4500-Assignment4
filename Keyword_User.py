import time
from selenium import webdriver
import collections
import csv

def findKeyword(driver, keyword)->bool:
    print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    #driver.get("http://172.21.1.251/pc4500/assignment1/")
    #driver.get("http://172.21.1.251/")
    reward_time = 10
    total_reward_time = 0;
    keyword = "student"
    if findKeyword(driver, keyword):
        total_reward_time += reward_time
        time.sleep(reward_time)
        
    driver.quit()
    print("Presence Time:", total_reward_time)
if __name__ == "__main__":
    main()