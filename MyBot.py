from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        self.options = webdriver.ChromeOptions()
        #location of chrome browser
        self.options.binary_location = "/usr/bin/google-chrome-stable"
        
        #location of chrome driver
        self.chrome_driver_path = "/usr/bin/chromedriver"
        
        self.bot = webdriver.Chrome(self.chrome_driver_path, options=self.options)


    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)


    def CloseBrowser(self):
        bot = self.bot
        bot.close()


    def searchHashtag(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)


    def likePhotos(self,amount):
        bot = self.bot

        bot.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i <= amount:
            time.sleep(2)
            #To press the Like button
            bot.find_element_by_class_name('fr66n').click()
            time.sleep(2)
            try:
                #To press the Follow button
                bot.find_element_by_class_name("bY2yH").click()
                try:
                    #if it already followed go unfollow him
                    bot.find_element_by_class_name("aOOlW").click()
                    time.sleep(1)
                except:
                    pass
                
            except:
                pass
            
            time.sleep(1)

            #To get the next post
        
            bot.find_element_by_class_name('coreSpriteRight').click()
            time.sleep(1)

            i += 1


insta = InstagramBot('username', 'password')
insta.login()
#specify any number of hashtags in the list
MyHashtags = ['coding', 'travel', 'instafun']

#looping throw all hashtags to like and follow every post containing this hashtag
for i in MyHashtags:
    insta.searchHashtag(i)
    time.sleep(2)
    #the number of posts you want to like and follow in my case it's 4
    insta.likePhotos(4)
    #if it's the last hashtag in the list call CloseBrowser method
    if i == MyHashtags[-1]:
        insta.CloseBrowser()
