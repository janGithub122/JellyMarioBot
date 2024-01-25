import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from numpy.random import choice


#Opening Game and Setting Up Chromedriver
url = 'https://jellymar.io/'
chrome_path = 'open -a /Applications/Google/ Chrome.app %s' #replace with whatever your path is
options = webdriver.ChromeOptions()
driver_location = r'put your driver path here'
service = Service(executable_path = driver_location)
driver = webdriver.Chrome(service = service, options = options)
driver.get(url)

#Random Key Bot Code
movement_button_list = [Keys.ARROW_UP, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.SPACE] #Adding the space key gives a chance for mario to explode

def random_key():
    while True:
        button = choice(movement_button_list, 1, p=[0.24995, 0.24995, 0.24995, 0.24995, 1/5000]) #changes the chance to press a certain key
        a = driver.find_element(By.TAG_NAME,'body').send_keys(button)
random_key()
