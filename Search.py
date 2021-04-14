from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def searcher(text):
    query  = text
    Path = "/Users/xaviernavarro/Documents/seleniumChromeDrive/chromedriver-2"

    driver = webdriver.Chrome(Path)
    driver.get("https://www.google.com/search?q=" + query)
    try:
        #if(driver.find_element(By.CSS_SELECTOR, ".Z0LcW").text):
        if (driver.find_element(By.CSS_SELECTOR, ".Z0LcW").text):
            #time.sleep(10)  # Let the user actually see something!
            place = ""
            place = driver.find_element(By.CSS_SELECTOR, ".Z0LcW").text
            print(place)
        elif(driver.find_element_by_class_name("FLP8od")):
            print("OK")
        else:
            print("not found")
            place = "I am sorry. I could not find anything. Try again."
    except:
        print(query + " had problems looking up for")
    return place
