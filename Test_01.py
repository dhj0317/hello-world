print("This is Test_01.py")

import time
import Objects
from selenium import webdriver


driver = webdriver.Chrome("/Users/Chris/Library/Selenium/chromedriver")
time.sleep(3)

driver.get("http://www.google.ca")
time.sleep(3)

driver.quit()
