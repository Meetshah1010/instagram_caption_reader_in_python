# import selenium,time & urllib modules
from selenium import webdriver
import time, urllib.request
import numpy as np

# launch Chrome and navigate to Instagram page
driver = webdriver.Chrome(executable_path=r'C:\Users\meet\Downloads\chromedriver_win32\chromedriver.exe')                 
driver.get("https://www.instagram.com/meet_shah_10_10/")

# scroll to the bottom of the page
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

# find all links on the page and if they match '/p' append to list named posts
posts = []
caps = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append( post )
print( posts )



download_url = ''
for post in posts:
  driver.get( post )
  cap = driver.find_element_by_xpath("//div[@class='C4VMK']/span").text
  caps.append(cap)
  print(cap)
  print("This post caption ended \n new will be generated further\n")
  
  
  
  time.sleep( 5 )
np.savetxt("array.txt",np.array(caps),fmt="%s")
print("Done")
driver.close()