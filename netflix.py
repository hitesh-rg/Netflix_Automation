from selenium import webdriver
import time
from Creds import LoginId, password

driver = webdriver.Chrome("C:\\Users\\Hitesh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

driver.get('https://netflix.com')
time.sleep(2)

signIn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/a').click()

#entering the registered email
emailId = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input')
emailId.send_keys(LoginId)
time.sleep(1)

#giving the password
passwordInput = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input')
passwordInput.send_keys(password)
time.sleep(1)

#logging in to the respective account
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()

#selecting user profile
time.sleep(3)
driver.find_element_by_link_text('Hitesh').click()

#movie_description
time.sleep(1)
synopsis = driver.find_elements_by_class_name('synopsis')
for value in synopsis:
    print(value.text)

#playing the trailer for 15 seconds
time.sleep(15)

#expanding the details for more information
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/button').click()
time.sleep(1)
