from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/admin_login'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):

        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        username=driver.find_element(By.CSS_SELECTOR,"input#email.input-text.required-entry.validate-email[title='Email Address']")
        username.send_keys("sougandh")
        password=driver.find_element(By.CSS_SELECTOR,"input#pass.input-text.required-entry.validate-password[title='Password']")
        password.send_keys("1234")
        time.sleep(2)
        submit=driver.find_element(By.CSS_SELECTOR,"button#send2.button.login[title='Login'][name='send'] > span")
        submit.click()
        time.sleep(4)
        redirect=driver.find_element(By.CSS_SELECTOR,"a.sidebar-link[href='/admin_assign_timeslots'] > span")
        redirect.click()
        time.sleep(4)
        input_date1 = "2023-12-10"
        formatted_date = datetime.strptime(input_date1, '%Y-%m-%d').strftime('%Y-%m-%d')
        opendate_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='date'][name='date'][required]")
        opendate_input.send_keys(formatted_date)
        time.sleep(1)
        select=driver.find_element(By.CSS_SELECTOR,"select.form-control[name='time_slots'][multiple][required]")
        select.click()
        time.sleep(4)
        slot=driver.find_element(By.CSS_SELECTOR,"option[value='morning']")
        slot.click()
        time.sleep(4)
        assign=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[type='submit']")
        assign.click()
        time.sleep(4)








        # driver = self.driver
        # driver.get(self.live_server_url)
        # driver.maximize_window()
        # time.sleep(1)
        # drop=driver.find_element(By.CSS_SELECTOR,"a.clicker[title='']")
        # drop.click()
        # time.sleep(2)
        # login=driver.find_element(By.CSS_SELECTOR,"a[title='My Account'][href='/login']")
        # login.click()
        # time.sleep(4)
        # email=driver.find_element(By.CSS_SELECTOR,"input#email.input-text.required-entry.validate-email[title='Email Address']")
        # email.send_keys("rijul@gmail.com")
        # password=driver.find_element(By.CSS_SELECTOR,"input#pass.input-text.required-entry.validate-password[title='Password']")
        # password.send_keys("Soug@123")
        # time.sleep(2)
        # submit=driver.find_element(By.CSS_SELECTOR,"button#send2.button.login[title='Login'][name='send'] > span")
        # submit.click()
        # time.sleep(4)
        # drop3=driver.find_element(By.CSS_SELECTOR,"a.level-top[href='/viewcar'] > span")
        # drop3.click()
        # time.sleep(3)
        # carview=driver.find_element(By.CSS_SELECTOR,"a.button.detail-bnt[href='/cardetail/1/'] > span")
        # carview.click()
        # time.sleep(2)
        # cardetail=driver.find_element(By.CSS_SELECTOR,"a.link-wishlist[href='/car_booking/1/'] > span")
        # cardetail.click()
        # time.sleep(2)
        # book=driver.find_element(By.CSS_SELECTOR,"button.button.btn-empty > span")
        # book.click()
        # time.sleep(2)



        








        # drop2=driver.find_element(By.CSS_SELECTOR,"a.clicker[title='']")
        # drop2.click()
        # time.sleep(2)
        # update=driver.find_element(By.CSS_SELECTOR,"a[title='My Account'][href='/update_profile']")
        # update.click()
        # time.sleep(4)
        # fname=driver.find_element(By.CSS_SELECTOR,"input#fname[type='text'][name='u_fname'][value='Rijul'][required]")
        # fname.clear()
        # fname.send_keys("Rijull")
        # time.sleep(1)
        # lname=driver.find_element(By.CSS_SELECTOR,"input#lname[type='text'][name='u_lname'][value='Roji'][required]")
        # lname.clear()
        # lname.send_keys("rojio")
        # time.sleep(1)
        # input_date1 = "2000-10-15"
        # formatted_date = datetime.strptime(input_date1, '%Y-%m-%d').strftime('%Y-%m-%d')
        # opendate_input = driver.find_element(By.CSS_SELECTOR, "input#date[type='date'][name='u_dob'][required]")
        # opendate_input.clear()
        # opendate_input.send_keys(formatted_date)
        # time.sleep(1)
        # contact=driver.find_element(By.CSS_SELECTOR,"input#contactinfo[type='text'][name='u_contact'][value='9384746754'][required]")
        # contact.clear()
        # contact.send_keys("9538857443")
        # time.sleep(1)
        # house=driver.find_element(By.CSS_SELECTOR,"input#house[type='text'][name='u_house'][value='Ponnattil'][required]")
        # house.clear()
        # house.send_keys("Ponnatil")
        # time.sleep(1)
        # place=driver.find_element(By.CSS_SELECTOR,"input#place[type='text'][name='u_place'][value='Kottayam'][required]")
        # place.clear()
        # place.send_keys("Pala")
        # time.sleep(1)
        # pincode=driver.find_element(By.CSS_SELECTOR,"input#pin[type='text'][name='u_pin'][value='686562'][required]")
        # pincode.clear()
        # pincode.send_keys("653898")
        # time.sleep(1)
        # file_path = 'C:\\Users\\souga\\Downloads'
        # thumbnail_image_input = driver.find_element(By.CSS_SELECTOR, "input#photo[type='file'][name='u_profile'][accept='image/*']")
        # thumbnail_image_input.clear()
        # thumbnail_image_input.send_keys(file_path)
        # time.sleep(3)
        # upbtn=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # upbtn.click()
        # time.sleep(4)



        



        
        # chat=driver.find_element(By.CSS_SELECTOR,"a.level-top[href='/chatwithadmin/'] > span")
        # chat.click()
        # time.sleep(2)
        # message=driver.find_element(By.CSS_SELECTOR,"textarea[name='feedback_message'][rows='5'][cols='50'][placeholder='Enter your Message here'][required]")
        # message.send_keys("Give me your Contact Details")
        # send=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # send.click()

        


        

    # Add more test methods as needed

if __name__ == '__main__':
    import unittest