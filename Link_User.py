import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
    

def main():
    start_time = time.time()
    presence_time = start_time

    driver = webdriver.Chrome()
    #driver.get("http://localhost:3000")
    
    #Acess To Web Pages From Internet
    #driver.get("http://47.149.102.253/pc4500/Sean/")
    #driver.get("http://47.149.102.253/pc4500/Rafael/")
    #driver.get("http://47.149.102.253/pc4500/ivanm/")
    #driver.get("http://47.149.102.253/pc4500/nicole/")
    
    #Acess To Web Pages From My Local Network
    #driver.get("http://172.21.1.251/pc4500/Sean/")
    #driver.get("http://172.21.1.251/pc4500/Rafael/")
    driver.get("http://172.21.1.251/pc4500/ivanmlast/")
    #driver.get("http://172.21.1.251/pc4500/nicole/")
    
    reward_time = 10
    total_reward_time = 0
    
    links = driver.find_elements(By.TAG_NAME,"a")
    total_links = len(links)
    print("Total Number Of links: ", total_links)

    current_time = time.time()
    presence_time = current_time - start_time
    total_reward_time = (reward_time*total_links) + presence_time
    print(f"Presence time: {presence_time} seconds")
    print(f"Reward time: {total_reward_time} seconds")

if __name__ == "__main__":
    main()
