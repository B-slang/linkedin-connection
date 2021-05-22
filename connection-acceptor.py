import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
# linkedin post liker
#
# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#
#
#
# To like other people's post:
# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb

email = os.environ.get('linkedin_user')
password = os.environ.get('linkedin_pass')

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://linkedin.com/login") 

driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)




driver.find_element_by_class_name("btn__primary--large").click()

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")



