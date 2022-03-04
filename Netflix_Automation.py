from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Hitesh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.netflix.com/in/title/81237994')
time.sleep(5)

#Printing the synopsis of the show
synopsis = driver.find_elements_by_class_name('title-info-synopsis')
for value in synopsis:
    print(value.text)

#Printing the cast 
cast = driver.find_elements_by_class_name('title-data-info-item-list')
for people in cast:
    print(people.text)

#Playing the trailer
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button/span[1]').click()