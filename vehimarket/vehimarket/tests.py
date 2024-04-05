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
        redirect=driver.find_element(By.CSS_SELECTOR,"a.sidebar-link[href='/adminaccessoriesadd'] > span")
        redirect.click()
        time.sleep(4)
        aname=driver.find_element(By.CSS_SELECTOR,"input#accessory_name[type='text'][name='accessory_name'][required]")
        aname.clear()
        aname.send_keys("Alloy")
        time.sleep(1)
        descrip=driver.find_element(By.CSS_SELECTOR,"input#description[type='text'][name='description'][required]")
        descrip.clear()
        descrip.send_keys("Very Nice Stylish Alloy")
        time.sleep(1)
        price=driver.find_element(By.CSS_SELECTOR,"input#price[type='text'][name='price'][required]")
        price.clear()
        price.send_keys("40000")
        time.sleep(1)
        brand=driver.find_element(By.CSS_SELECTOR,"input#brand[type='text'][name='brand'][required]")
        brand.clear()
        brand.send_keys("BBS")
        time.sleep(1)
        atype=driver.find_element(By.CSS_SELECTOR,"select#category[name='category']")
        atype.click()
        atypeselect=driver.find_element(By.CSS_SELECTOR,"option[value='exterior']")
        atypeselect.click()
        time.sleep(1)
        quant=driver.find_element(By.CSS_SELECTOR,"input#quantity[type='number'][name='quantity'][required]")
        quant.clear()
        quant.send_keys("20")
        time.sleep(1)
        warr=driver.find_element(By.CSS_SELECTOR,"input#warranty[type='number'][name='warranty'][required]")
        warr.clear()
        warr.send_keys("5")
        time.sleep(1)
        file_path = 'C:\\Users\\souga\\Downloads\\bbs1.png'
        thumbnail_image_input = driver.find_element(By.CSS_SELECTOR, "input#images1[type='file'][name='images1']")
        thumbnail_image_input.send_keys(file_path)
        time.sleep(3)
        file_path2 = 'C:\\Users\\souga\\Downloads\\bbs2.png'
        thumbnail_image_input2 = driver.find_element(By.CSS_SELECTOR, "input#images2[type='file'][name='images2']")
        thumbnail_image_input2.send_keys(file_path2)
        time.sleep(3)
        file_path3 = 'C:\\Users\\souga\\Downloads\\bbs3.png'
        thumbnail_image_input3 = driver.find_element(By.CSS_SELECTOR, "input#images3[type='file'][name='images3']")
        thumbnail_image_input3.send_keys(file_path3)
        time.sleep(3)
        file_path4 = 'C:\\Users\\souga\\Downloads\\bbs4.png'
        thumbnail_image_input4 = driver.find_element(By.CSS_SELECTOR, "input#images4[type='file'][name='images4']")
        thumbnail_image_input4.send_keys(file_path4)
        time.sleep(3)
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
        submit_button.click()
        time.sleep(5)


        







        
        
        # redirect=driver.find_element(By.CSS_SELECTOR,"a.sidebar-link[href='/admin_assign_timeslots'] > span")
        # redirect.click()
        # time.sleep(4)
        # input_date1 = "2023-12-10"
        # formatted_date = datetime.strptime(input_date1, '%Y-%m-%d').strftime('%Y-%m-%d')
        # opendate_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='date'][name='date'][required]")
        # opendate_input.send_keys(formatted_date)
        # time.sleep(1)
        # select=driver.find_element(By.CSS_SELECTOR,"select.form-control[name='time_slots'][multiple][required]")
        # select.click()
        # time.sleep(4)
        # slot=driver.find_element(By.CSS_SELECTOR,"option[value='morning']")
        # slot.click()
        # time.sleep(4)
        # assign=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[type='submit']")
        # assign.click()
        # time.sleep(4)








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