import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#This class used to contain the href text and url it will lead to
class linking: 
    def __init__(self, href, url):
        self.href = href
        self.url = url

Mainpage_url = "http://localhost:3000"

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Mainpage_url)

    def test_link_in_main_page(self):
        #Load all the url and href needed testing in this array
        href_url = []
        href_url.append(linking("#zingchart","http://localhost:3000/zing-chart"))
        href_url.append(linking("Radio","http://localhost:3000/radio"))
        href_url.append(linking("BXH Nhạc Mới","http://localhost:3000/moi-phat-hanh"))
        href_url.append(linking("Chủ Đề & Thể Loại","http://localhost:3000/hub"))
        href_url.append(linking("Top 100","http://localhost:3000/top100"))                
                    

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)


        #Checks if the links work
        for i in href_url:
            check = self.driver.find_element(By.LINK_TEXT,i.href)
            action = ActionChains(self.driver)
            action.click(check)
            action.perform()
            self.assertTrue(self.driver.current_url == i.url)
            self.driver.back()


        #The rest is true
        self.assertTrue

    def test_login_popup(self):
        main_page = page.MainPage(self.driver)        
        check = self.driver.find_element(By.LINK_TEXT,"Thư Viện")
        action = ActionChains(self.driver)
        action.click(check)
        action.perform()
        self.assertTrue(self.driver.find_element(By.NAME,"email").is_displayed)
       

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()