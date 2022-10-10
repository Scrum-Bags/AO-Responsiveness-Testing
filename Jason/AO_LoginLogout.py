from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from AO_Locators import AO_Login_Objects
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
import time

#https://selenium-python.readthedocs.io/getting-started.html#simple-usage

class AO_Login():


    def __init__(self, driver = "default"):

        if(driver=="default"):
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver


    def Launch_Login_Page(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((AO_Login_Objects.By_load_screen)))
            WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((AO_Login_Objects.By_load_screen)))
        except:
            pass

    def MobileCheck(self):
        #print(self.driver.find_element(*AO_Login_Objects.By_login_menu).size["height"])
        return not self.driver.find_element(*AO_Login_Objects.By_login_menu).size["height"] > 0

    def AO_login(self, reporter, ssPath, username, password):
        print("***Logging into Advantage Online***")
        driver = self.driver

        #print("5555555555555555555555555555555555555555555555555555555555555555555")
        #print(self.MobileCheck())
        mobile = self.MobileCheck()

        #determine if mobile dropdown is present
        if mobile:
            #print(len(driver.find_elements(*AO_Login_Objects.By_mobile_dropdown)))
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Login_Objects.By_mobile_dropdown)))
            driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            time.sleep(1)
            reporter.reportStep("Locate login dropdown","Login dropdown should be locatable","Login dropdown located",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            driver.find_element(*AO_Login_Objects.By_login_menu_m).click()
        else:
            #print(len(driver.find_elements(*AO_Login_Objects.By_login_menu)))
            try:
                #print(len(driver.find_elements(*AO_Login_Objects.By_login_menu)))
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_menu)))
                reporter.reportStep("Locate login dropdown","Login dropdown should be locatable","Login dropdown located",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
                driver.find_element(*AO_Login_Objects.By_login_menu).click()
            except:
                reporter.reportStep("Locate login dropdown","Login dropdown should be locatable","Unable to locate login dropdown",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
                print("Unable to locate login dropdown")
                return False

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_field)))


        self.username_field = self.driver.find_element(*AO_Login_Objects.By_login_field)
        self.password_field = self.driver.find_element(*AO_Login_Objects.By_password_field)
        elem1 = self.username_field
        elem1.send_keys(username)
        if elem1.get_attribute('value') == username:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username successfully placed in dialog box",True,username, driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Username successfully placed in dialog box")
        else:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username not placed in dialog box",False,username, driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Username not placed in dialog box")
            return False
        #short pause for password field
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_password_field)))
        elem2 = self.password_field
        elem2.send_keys(password)
        
        if elem2.get_attribute('value') == password:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password successfully placed in dialog box",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Password successfully placed in dialog box")
        else:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password not place in dialog box",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Password not place in dialog box")
            return False
        
        if driver.find_element(*AO_Login_Objects.By_remember_user).is_selected():
            driver.find_element(*AO_Login_Objects.By_remember_user).click()
        print("Clicking login button")
        elem2.send_keys(Keys.RETURN)
        #confirm login
        if not mobile:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_user_menu)))
        else:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_mobile_dropdown)))
            #driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            #WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((AO_Login_Objects.By_user_menu_m_indicator), username))
        #time.sleep(1)
        if len(driver.find_elements(*AO_Login_Objects.By_user_menu))>0:
            reporter.reportStep("Press submit and login","User dashboard should appear","Login successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Login successful")
        else:
            reporter.reportStep("Press submit and login","User dashboard should appear","Login unsuccessful",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Login unsuccessful")
            print("meeeepeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return False
            
        self.username=username
        self.password=password
        print("***End of Logging into Advantage Online***")
        return True

    def AO_login_remember_test(self, reporter, ssPath, username, password):
        driver = self.driver

##        while len(self.driver.find_elements(*AO_Login_Objects.By_login_menu))==0:
##            #loop until load
##            pass
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_menu)))

        driver.find_element(*AO_Login_Objects.By_login_menu).click()


##        while len(self.driver.find_elements(*AO_Login_Objects.By_login_field))==0:
##            #loop until load
##            pass
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_field)))
        
        self.username_field = self.driver.find_element(*AO_Login_Objects.By_login_field)
        self.password_field = self.driver.find_element(*AO_Login_Objects.By_password_field)

        elem1 = self.username_field
        elem1.send_keys(username)
        if elem1.get_attribute('value') == username:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username successfully placed in dialog box",True,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username not place in dialog box",False,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        #short pause for password field
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_password_field)))
        elem2 = self.password_field
        elem2.send_keys(password)
        
        if elem2.get_attribute('value') == password:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password successfully placed in dialog box",True,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password not place in dialog box",False,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
       
        rememberObj = driver.find_element(*AO_Login_Objects.By_remember_user)
        if rememberObj.is_selected() == False:
            rememberObj.click()

        #THIS SLEEP WORKS, REPLACE WITH A WEBDRIVERWAIT SOMEHOW
        elem2.send_keys(Keys.RETURN)
        #WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_user_menu)))
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
        #time.sleep(8)
        
        if len(driver.find_elements(*AO_Login_Objects.By_user_menu))>0:
            reporter.reportStep("Press submit and login","User dashboard should appear","Login successful",True,"", driver.find_element(*AO_Login_Objects.By_user_menu).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Press submit and login","User dashboard should appear","Login unsuccessful",False,"", driver.find_element(*AO_Login_Objects.By_user_menu).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))

        self.username=username
        self.password=password

##        #refresh the page
##        driver.get("https://www.advantageonlineshopping.com/#/")
##        time.sleep(3)
        self.Launch_Login_Page()

        
        
        if len(driver.find_elements(*AO_Login_Objects.By_user_menu))>0:
            reporter.reportStep("Refresh page after logging in","User dashboard should appear","Remember user successful",True,"", driver.find_element(*AO_Login_Objects.By_user_menu).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            #signout
            self.AO_logout(reporter, ssPath)
            #time.sleep(5)
        else:
            reporter.reportStep("Refresh page after logging in","User dashboard should appear","Remember user unsuccessful",False,"", driver.find_element(*AO_Login_Objects.By_user_menu).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))

        #refresh the page
        #driver.get("https://www.advantageonlineshopping.com/#/")
        #time.sleep(5)
        
        #check that username, password, and remember_me are still there
##        while len(driver.find_elements(*AO_Login_Objects.By_login_menu))==0:
##            #loop until load
##            pass
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((AO_Login_Objects.By_load_screen)))
            WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((AO_Login_Objects.By_load_screen)))
        except:
            pass
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_menu)))
        driver.find_element(*AO_Login_Objects.By_login_menu).click()
        #driver.find_element(*AO_Login_Objects.By_login_menu).click()
##        while len(driver.find_elements(*AO_Login_Objects.By_login_field))==0:
##            #loop until load
##            pass
##        #hard wait for screenshots
##        time.sleep(10)
        #print("waiting for it to appear")
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((AO_Login_Objects.By_login_field)))

        
        elem1 = driver.find_element(*AO_Login_Objects.By_login_field)
        elem2 = driver.find_element(*AO_Login_Objects.By_password_field)
        #check values in login field
        if elem1.get_attribute('value') == username:
            reporter.reportStep("Check value in username field","Username should appear in the dialog box","Username successfully placed in dialog box",True,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Check value in username field","Username should appear in the dialog box","Username not place in dialog box",False,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        if elem2.get_attribute('value') == password:
            reporter.reportStep("Check value in password field","Password should appear in the dialog box","Password successfully placed in dialog box",True,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Check value in password field","Password should appear in the dialog box","Password not place in dialog box",False,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        if driver.find_element(*AO_Login_Objects.By_remember_user).is_selected():
            reporter.reportStep("Get value of 'remember me' button","The 'remember me' button is still checked","'Remember me' is true",True,"", driver.find_element(*AO_Login_Objects.By_remember_user).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            driver.find_element(*AO_Login_Objects.By_remember_user).click()
        else:
            reporter.reportStep("Get value of 'remember me' button","The 'remember me' button is still checked","'Remember me' is false",False,"", driver.find_element(*AO_Login_Objects.By_remember_user).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        #log back in with remember me disabled to reset state for future tests
        elem2.send_keys(Keys.RETURN)
##        time.sleep(3)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_user_menu)))
        self.AO_logout(reporter, ssPath)
        #driver.find_element(*AO_Login_Objects.By_close_login_menu).click()

    def AO_logout(self, reporter, ssPath):
        print("***Logging out of Advantage Online***")
        driver = self.driver
        #driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        mobile = self.MobileCheck()

        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))

        #determine if mobile dropdown is present
        if mobile:
            #print(len(driver.find_elements(*AO_Login_Objects.By_mobile_dropdown)))
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Login_Objects.By_mobile_dropdown)))
            driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_user_menu_m)))
            driver.find_element(*AO_Login_Objects.By_user_menu_m).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_sign_out_m)))
            driver.find_element(*AO_Login_Objects.By_sign_out_m).click()
            mobile = True
        else:
            driver.find_element(*AO_Login_Objects.By_user_menu).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_sign_out)))
            driver.find_element(*AO_Login_Objects.By_sign_out).click()

        if len(driver.find_elements(*AO_Login_Objects.By_login_menu))>0:
            reporter.reportStep("Press logout button","Login button should appear","Logout successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Logout successful")
        else:
            reporter.reportStep("Press logout button","Login button should appear","Logout unsuccessful",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Logout unsuccessful")
        self.username=""
        self.password=""
        print("***End of Logging out of Advantage Online***")

    def AO_bad_login(self, reporter, ssPath, username, password):
        driver = self.driver

        if username is None:
            username = ""
        if password is None:
            password = ""
        
        #check that menu exists
##        while len(self.driver.find_elements(*AO_Login_Objects.By_login_menu))==0:
##            #loop until load
##            pass
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_menu)))
        driver.find_element(*AO_Login_Objects.By_login_menu).click()
        #check that login field exists
##        while len(self.driver.find_elements(*AO_Login_Objects.By_login_field))==0:
##            #loop until load
##            pass
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_field)))
        #enter username and password
        self.username_field = self.driver.find_element(*AO_Login_Objects.By_login_field)
        self.password_field = self.driver.find_element(*AO_Login_Objects.By_password_field)
        elem1 = self.username_field
        elem1.send_keys(username)
        #check that username was entered
        if elem1.get_attribute('value') == username:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username successfully placed in dialog box",True,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username not place in dialog box",False,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        #short pause for password field
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_password_field)))
        self.password_field.click()
        time.sleep(1)
        #check for input error message if username is blank
        error = driver.find_elements(*AO_Login_Objects.By_login_field_error)
        if username=="":
            if len(error)>0:
                reporter.reportStep("Login with blank username","Error message should appear","Error message appeared",True,error[0].text, error[0].screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            else:
                reporter.reportStep("Login with blank username","Error message should appear","Error did not appear",False,"")

        elem2 = self.password_field
        elem2.send_keys(password)
        #check that password was entered
        if elem2.get_attribute('value') == password:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password successfully placed in dialog box",True,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Put password in dialog box","Password should appear in the dialog box","Password not place in dialog box",False,password, elem2.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))

        self.username_field.click()
        time.sleep(1)
        #check for input error message if password is blank
        error = driver.find_elements(*AO_Login_Objects.By_password_field_error)
        if password=="":
            if len(error)>0:
                reporter.reportStep("Login with blank password","Error message should appear","Error message appeared",True,error[0].text, error[0].screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            else:
                reporter.reportStep("Login with blank password","Error message should appear","Error did not appear",False,"")

        driver.find_element(*AO_Login_Objects.By_sign_in).click()
        time.sleep(3)

        if password!="" and username!="":
        #check for error message
            if len(driver.find_elements(*AO_Login_Objects.By_sign_in_error))>0 and driver.find_elements(*AO_Login_Objects.By_sign_in_error)[0].text != "OR":
                error = driver.find_element(*AO_Login_Objects.By_sign_in_error)
                reporter.reportStep("Login with bad credentials","Error message should appear","Error message appeared",True,error.text, error.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            else:
                reporter.reportStep("Login with bad credentials","Error message should appear","Error did not appear",False,"")

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_close_login_menu)))
        driver.find_element(*AO_Login_Objects.By_close_login_menu).click()

        
    def AO_forgot_password(self, reporter, ssPath, username):
        driver = self.driver

        if username is None:
            username = ""

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_menu)))
        driver.find_element(*AO_Login_Objects.By_login_menu).click()

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_login_field)))
        #enter username and password
        self.username_field = self.driver.find_element(*AO_Login_Objects.By_login_field)
        elem1 = self.username_field
        elem1.send_keys(username)
        #check that username was entered
        if elem1.get_attribute('value') == username:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username successfully placed in dialog box",True,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Put username in dialog box","Username should appear in the dialog box","Username not place in dialog box",False,username, elem1.screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Login_Objects.By_forgot_password_link)))
        driver.find_element(*AO_Login_Objects.By_forgot_password_link).click()
        time.sleep(5)

        if len(driver.find_elements(*AO_Login_Objects.By_forgot_password_link))>0:
            reporter.reportStep("Press forgot password button","Site should navigate to a forgot password page","Navigation unsuccessful",False,"", driver.find_element(*AO_Login_Objects.By_forgot_password_link).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
        else:
            reporter.reportStep("Press forgot password button","Site should navigate to a forgot password page","Navigation successful",True,"", driver.find_element(*AO_Login_Objects.By_forgot_password_link).screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
      
