from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
import selenium
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import *
import datetime
import math
import os
import string
import urllib
from progress.bar import Bar
####################################CHANGE HERE#####################################
newpath = '/home/username/Desktop/internship/follower_links'
if not os.path.exists(newpath):
    os.makedirs(newpath)
printable= set(string.printable)
# Open up a browser and navigate to web page.
####################################CHANGE HERE#####################################
browser = webdriver.Chrome('/home/username/Downloads/chromedriver_linux64/chromedriver')
k=0
count=0
####################################CHANGE HERE#####################################
with open('usernames.txt') as f:
    content = f.readlines()
l=[]

content = [x.strip() for x in content] 
for i in range(0,len(content)):
	if os.path.exists(newpath+'/'+content[i]):
		print content[i]+'already done'
		continue 
	
	if not os.path.exists(newpath+'/'+content[i]):
		os.makedirs(newpath+'/'+content[i])
	
	url = 'https://www.instagram.com/'+content[i]+ '/'
	num=1
	browser.get(url)
	SCROLL_PAUSE_TIME = 1
	k = 0
	posts_collected = 0
	posts=0
	flag1 = 0
	temp = 0
	#### XPATH to first post one user's page: //*[@id="react-root"]/section/main/div/div/article/div[1]/div/div[1]/div[1]/a
	#### XPATH to number of posts on user's page: //*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span
	try:
		no_of_posts = ui.WebDriverWait(browser, 3).until(lambda browser:browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span')).text.replace(',','')
	except:
		not_exits_file = open('not_done.txt','a+')
		not_exits_file.write(content[i])
		not_exits_file.close()
		continue
	print 'total post for '+content[i]+': '+no_of_posts
	file = open(newpath+'/'+content[i]+'/'+content[i]+".txt",'w+')
	try:
		first_post = ui.WebDriverWait(browser, 3).until(lambda browser:browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div[1]/div[1]/a'))
	except:
		private_user_file = open('private.txt','a+')
		private_user_file.write(content[i])
		private_user_file.close()
		continue
	file.write(no_of_posts)
	first_post.send_keys(Keys.TAB)
	link = browser.switch_to_active_element()
	count = 0
	prev_link = None
	bar = Bar(content[i], max = min(1000,int(no_of_posts)))
	while posts_collected < int(no_of_posts) - 1 and posts_collected < 1000:
		#print link
		href_link = link.get_attribute('href')
		#print href_link
		if href_link == 'https://www.instagram.com/':
			#driver.find_element_by_xpath('//a[@href="'+variable+'"]');
			link = browser.find_element_by_xpath('//a[@href="'+prev_link[25:]+'"]')
			#print 'hey hey hey'
			#print link
			link.send_keys(Keys.TAB)
			link = browser.switch_to_active_element()
			time.sleep(1)
			'''
			link.send_keys(Keys.SHIFT+Keys.TAB)
			time.sleep(3)
			'''
			count+=1
			if count == 30:
				#time.sleep(4)
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(5)
				x_result = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/div/a[1]')
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.UP)
				x_result = browser.switch_to_active_element()
				time.sleep(5)
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				x_result.send_keys(Keys.DOWN)
				x_result = browser.switch_to_active_element()
				time.sleep(3)
				#browser.execute_script("window.scrollTo(0, -100);")
				#time.sleep(2)
			continue
		count = 0
		prev_link = href_link
		file.write(href_link)
		file.write('\n')
		link.send_keys(Keys.TAB)
		link = browser.switch_to_active_element()
		#count +=1
		posts_collected +=1
		bar.next()
	bar.finish()
	
