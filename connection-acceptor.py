import os
# from time import sleep
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# pip install selenium && pip install webdriver_manager && pip install tinydb

# fetching from os.env 

email = os.environ.get('linkedin_user')
password = os.environ.get('linkedin_pass')

# if chrome not in your pc
driver = webdriver.Chrome(ChromeDriverManager().install())

# login
driver.get("https://linkedin.com/login") 

# sending pass n email from above email n passowrd
driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)



# signin button
driver.find_element_by_css_selector(".btn__primary--large").click()

# url
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

# connection hi nai h to pata nai chalra kaam kar rha h ye ki nai copy at your own risk
button = []
while len(button) == 0:
    button = driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")

# traversal in connectpepul
for pepul in button:
    pepul.click()
    time.sleep(3)
