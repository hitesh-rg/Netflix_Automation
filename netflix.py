from selenium import webdriver
import time
from Creds import LoginId, password

driver = webdriver.Chrome("C:\\Users\\Hitesh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

driver.get('https://netflix.com')
time.sleep(2)

signIn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/a').click()
emailId = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input')
emailId.send_keys(LoginId)
time.sleep(1)

passwordInput = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input')
passwordInput.send_keys(password)
time.sleep(1)

driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()

driver.find_element_by_link_text('Hitesh').click()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a').click()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/span').click()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]').click()
#input_profile = driver.find_element_by_class_name('profile-name')

#driver.find_elements_by_class_name('profile-name').click()
#input_profile = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]').click()
#print(input_profile)