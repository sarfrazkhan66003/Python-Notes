# import selenium 
# print("Facebook automation")
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
sleep(5)
driver.get('https://facebook.com')
sleep(5)
element = driver.find_element('id','email')
#element.send_keys('sarfrazkhan66003@gmail.com')
username = 'sarfrazkhan66003@gmail.com'
for c in username:
      element.send_keys(c)
      sleep(0.5)
      
sleep(5)
element = driver.find_element('id','pass')
element.send_keys('sarfraz@0786')
log = driver.find_element('name','login')
log.click()
sleep(5)
driver.get('https://facebook.com/friends/list')
sleep(150)