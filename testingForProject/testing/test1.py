import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SimpleTest(unittest.TestCase):
    def test1_signInSignOut(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #clicking sign in
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/main/div/p').text, 'welcome '+userName, "matched")  # should not be passed

        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #logout button click
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').text,'Sign In' , "matched")  # should not be passed


        self.driver.quit()


if __name__ == '__main__':
    unittest.main()