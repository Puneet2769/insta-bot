from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagrambot:

    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path='YOUR PATH WHERE GECKODRIVER>EXE LOCATED')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')

        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)


    def like(self,hashtag):
        count = 0
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'')
        time.sleep(2)


    def likephotos(self,amount):
        bot = self.bot
        bot.find_elements_by_class_name('_9AhH0')[0].click()

        i = 1
        time.sleep(5)
        while i <= amount:
            time.sleep(2)
            bot.find_elements_by_css_selector('.fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')[0].click()
            bot.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
            i += 1
            
        

        bot.get('https://instagram.com/' + self.username)




insta = instagrambot('your username','your password')
insta.login()
insta.like('hashtag u like but dont add hastag sign')
insta.likephotos(25)#number can be edited i done 25 u can like as many photos u want
# but after 25 photos instagram stops u



         
