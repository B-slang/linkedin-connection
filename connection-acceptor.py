import os
from time import sleep
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from config import dotenv_values
 
# linkedin post liker
#
# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#
#
#
# To like other people's post:
# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb

email=os.environ.get('LINKEDIN_EMAIL')
password=os.environ.get('LINKEDIN_password')
driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)

 
# # step 1 change this from : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
links = [

    "https://www.linkedin.com/mynetwork/"

    ]
#     "https://www.linkedin.com/posts/sidd-oo_100daysofcode-devsnestday21-devsnest6monthschallenge-activity-6789459261542973440-x7FX/",
#     "https://www.linkedin.com/posts/ross-nelson-32493684_devsnest6monthschallenge-devsnestday21-slowandsteady-activity-6788661474186338304-Dx0z"

#step 2 : run code , check if you are logged in (if not, then login) then press 1 in console
#step 3 : the code shoud take care of the rest add your posts that you would want to get liked
 
 
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")
# delete this after every month
