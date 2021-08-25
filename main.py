from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https://www.youtube.com/watch?v=d2GBO_QjRlo&t=44s - Building a simple Instagram bot with Python tutorial
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)      
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(6)
   		# first pop-up 
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
            .click()
        sleep(15)
   		# 2nd pop-up 
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        sleep(8)
       

    def get_followers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")\
            .click()
        sleep(5)
        #followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()       
        followers = self._get_names()        

    def _get_names(self):
      
        sleep(5)
        # uuidArray = []
        # NoElementError = []
        # scroll_box = self.driver.find_element_by_class_name("isgrP")
        # https://stackoverflow.com/questions/60955765/how-to-get-followers-list-in-instagram-using-selenium-in-python
        self.driver.execute_script('''
        var scroll_box = document.querySelector('div[role="dialog"] .isgrP');
        scroll_box.scrollTop = scroll_box.scrollHeight
        ''')
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
        # scroll_box.send_keys(Keys.END)
        # selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable


        # /html/body/div[5]/div/div/div[2]/ul 2nd level down.
        # last_ht, ht = 0, 1
        # while last_ht != ht:
        #     last_ht = ht
        #     sleep(1)
        #     ht = self.driver.execute_script("""
        #         arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        #         return arguments[0].scrollHeight;
        #         """, scroll_box)

        # # after click follower link, wait until dialog appear
        # WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
        # # now scroll
        # self.driver.execute_script('''
        #     var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        #     fDialog.scrollTop = fDialog.scrollHeight
        # ''')

        # sleep(1)
        # scr1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[12]")
        # # scr1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[%s]" % i)
        # self.driver.execute_script("arguments[0].scrollIntoView();", scr1)
        # sleep(1) 
        # last_ht, ht = 0, 1
        # while last_ht != ht:
        #     last_ht = ht
        #     sleep(1)
        #     ht = self.driver.execute_script("""
        #         arguments[0].scrollTo(0, arguments[0].scrollHeight);
        #         return arguments[0].scrollHeight;   
        #         """, scr1)       

        # https://github.com/aarnhub/instagram-scraper-python/blob/master/followers-scraper.py
        # for i in list(range(1,3446)):
        #     try:
        #         sleep(1)
        #         scr1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[12]")
        #         # scr1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[%s]" % i)
        #         self.driver.execute_script("arguments[0].scrollIntoView();", scr1)
        #         sleep(1) 
        #         last_ht, ht = 0, 1
        #         while last_ht != ht:
        #             last_ht = ht
        #             sleep(1)
        #             ht = self.driver.execute_script("""
        #                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
        #                 return arguments[0].scrollHeight;   
        #                 """, scr1)       

        #         # links = scr1.find_elements_by_tag_name('a')
        #         # names = [name.text for name in links if name.text != '']
        #         # uuidArray.append(names)
        #         # print(uuidArray)  
        #     except NoSuchElementException as e:
        #         # raise e
        #         print(e)
        #         continue 
        #         # print(uuidArray)  
        #         # sleep(6)
        #         # continue 
        #         # print("Error")
        #         # NoElementError.append('Error')
        #         # if(NoElementError == 5):
        #         #     break
        #         # sleep(1)
        #         # continue
        #     except StaleElementReferenceException as e:
        #         # raise e
        #         print(e)
        #         continue
                # pass
                # continue
            # print(NoElementError)    
            # except:
                # handle the element not existing  
                # uuidArray.append(None)
                # print(i)
                # sleep(1)
                # continue
                # print(i)
                # sleep(5)
                # element = WebDriverWait(self.driver, 10).until(
                # https://stackoverflow.com/questions/60395570/invalidargumentexception-message-invalid-argument-using-must-be-a-string    
                # EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/ul/div/li[%s]" % i))
                #                                          )
                # print(element)                                                                                                  
                # self.driver.execute_script("arguments[0].scrollIntoView();", "/html/body/div[5]/div/div/div[2]/ul/div/li[%s]" % i)
                # sleep(1)
                # links = scr1.find_elements_by_tag_name('a')
                # names = [name.text for name in links if name.text != '']
                # uuidArray.append(names)
                # print(uuidArray)                                          
      

        
                                

my_bot = InstaBot('username', 'password')
my_bot.get_followers()