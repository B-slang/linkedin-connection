import os
from time import sleep
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
driver.find_element_by_class_name("btn__primary--large").click()

# url
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

# connection hi nai h to pata nai chalra kaam kar rha h ye ki nai copy at your own risk
connectpepul = []
while len(connectpepul) == 0:
    connectpepul = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div/div/div/main/section/div[2]/section/div/ul/li/div[1]/div[2]/button[2]")

# traversal in connectpepul
for pepul in connectpepul:
    pepul.click()
