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
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")  # should be passed

        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #logout button click
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').text,'Sign In' , "matched")  # should be passed


        self.driver.quit()

    def test2_signup(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test2'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click() #clicking signup
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[1]/div/input').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/div/input').send_keys("niamul2@gmail.com")# giving email
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[3]/div/input').send_keys(
            "abcd1234@123")  # giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[4]/div/input').send_keys(
            "abcd1234@123")  # giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[5]/div/input').send_keys(
            "01704159550")  # giving mobile num
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').click() #clicking signup
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")
        self.assertEqual(self.driver.find_element(By.XPATH, '/ html / body / div / div / div / div[1] / form / p[1]').text, "Activate your account:", "matched") # should be passed


        self.driver.quit()





    def test3_adView(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #clicking sign in
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")  # should not be passed

        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/p').click() #click on first AD
        time.sleep(2)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div').text, 'Contact seller', "matched")


        self.driver.quit()


    def test5_adViewWithOutSignIn(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')


        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/p').click() #click on first AD
        time.sleep(4)

        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/p[1]').text, 'User Name:', "matched")


        self.driver.quit()

    def test6_PostAD(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #clicking sign in
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")  # should not be passed

        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[3]/a').click() #clicking post AD
        time.sleep(4)

        self.driver.find_element(By.XPATH, '//*[@id="id_title"]').send_keys("sample title") #puting title
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[2]/div/select/option[6]').click() # selecting location
        self.driver.find_element(By.XPATH, '//*[@id="id_sqft"]').send_keys("1600")  # putting sqft
        self.driver.find_element(By.XPATH, '//*[@id="id_washRoom"]').send_keys("3")  #washroom
        self.driver.find_element(By.XPATH, '//*[@id="id_bedRoom"]').send_keys("3")  #bedRoom


        self.driver.find_element(By.XPATH, '//*[@id="id_description"]').send_keys("good")  # description


        self.driver.find_element(By.XPATH, '//*[@id="id_roadSize"]').send_keys("12")# roadsize


        self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[11]/div/select/option[3]').click()#lift service

        self.driver.find_element(By.XPATH, '//*[@id="id_floor"]').send_keys("7")  # floor
        self.driver.find_element(By.XPATH, '//*[@id="id_price"]').send_keys("10000000")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/form/div/input').click()  # lift service



        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p[2]').text,'Your AD is posted' , "matched")  # should be passed


        self.driver.quit()


    def test7_PostAD_WithIntentionallyError(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #clicking sign in
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")  # should not be passed

        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[3]/a').click() #clicking post AD
        time.sleep(4)

        self.driver.find_element(By.XPATH, '//*[@id="id_title"]').send_keys("sample title") #puting title
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[2]/div/select/option[6]').click() # selecting location
        self.driver.find_element(By.XPATH, '//*[@id="id_sqft"]').send_keys("1600")  # putting sqft
        self.driver.find_element(By.XPATH, '//*[@id="id_washRoom"]').send_keys("3")  #washroom
        self.driver.find_element(By.XPATH, '//*[@id="id_bedRoom"]').send_keys("3")  #bedRoom


        self.driver.find_element(By.XPATH, '//*[@id="id_description"]').send_keys("good")  # description


        self.driver.find_element(By.XPATH, '//*[@id="id_roadSize"]').send_keys("12")# roadsize


        self.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div/div[11]/div/select/option[3]').click()#lift service

        self.driver.find_element(By.XPATH, '//*[@id="id_floor"]').send_keys("7")  # floor
        self.driver.find_element(By.XPATH, '//*[@id="id_price"]').send_keys("10000000")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/form/div/input').click()  # lift service



        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p[2]').text,'Your AD is' , "matched")  # should be passed


        self.driver.quit()

    def test8_PredictingHousePrice(self):

        self.driver = webdriver.Firefox(executable_path="c:/Sel_Firefox/geckodriver.exe")
        self.driver.get('http://niamul26.pythonanywhere.com/')

        userName='test'
        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click() #clicking sign in
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys(userName) #puting user name
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("testingsignin")# giving password
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').click() #clicking login
        time.sleep(4)
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/div/div/div/p').text, 'welcome '+userName, "matched")  # should  be passed

        self.driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click() #predict button click
        time.sleep(4)

        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/select[1]/option[3]').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[2]').send_keys("1811") #sqrt
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[3]').send_keys("3")  # washRoom
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[4]').send_keys("3")  # bedRomm
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[5]').send_keys("7")  # floor
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[5]').send_keys("7")  # floor
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/select[2]/option[3]').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[6]').send_keys("27")  # floor
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/input[7]').click()






        self.assertEqual(self.driver.find_element(By.XPATH, '/ html / body / div / div / div / div / form / p[1] / span[1]').text,'The price of an apartment is around:' , "matched")  # should be passed


        self.driver.quit()
if __name__ == '__main__':
    unittest.main()