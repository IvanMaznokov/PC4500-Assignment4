import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def countElem(driver, tag_name)->int:
    #tag_name = "img"
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    #driver.get("http://localhost:3000/")
    #driver.get("http://172.21.1.251/pc4500/assignment1/")
    driver.get("http://172.21.1.251/pc4500/test.txt")
    reward_time = 10
    total_reward_time = 0;
    tags = ["img"]
    for tag in tags:
        num_images = countElem(driver, tag)
        total_reward_time += reward_time*num_images
        time.sleep(reward_time)    
    driver.quit()
    print("Presence Time:", total_reward_time, " seconds")
if __name__ == "__main__":
    main()