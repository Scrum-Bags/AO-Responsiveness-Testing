from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class AO_Login_Objects(object):
    #mobile link to login objects
    By_mobile_dropdown = (By.ID, "mobile-btn")
    By_login_menu_m = (By.ID, "mobileUser")
    #link to login objects
    By_login_menu = (By.XPATH, "//*[@id='menuUser']")
    #objects on login page
    By_login_field = (By.NAME, 'username')
    By_password_field = (By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/input")
    By_sign_in = (By.XPATH, "//*[@id='sign_in_btnundefined']")
    By_sign_in_error = (By.XPATH, "//*[@id='signInResultMessage']")
    By_login_field_error = (By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/label")
    By_password_field_error = (By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/label")
    By_forgot_password_link = (By.XPATH, "/html/body/login-modal/div/div/div[3]/a[1]")
    By_create_account_link = (By.XPATH, "/html/body/login-modal/div/div/div[3]/a[2]")
    By_close_login_menu = (By.XPATH, "/html/body/login-modal/div/div/div[2]")
    By_remember_user = (By.NAME, 'remember_me')
    #objects in user menu
    By_user_menu = (By.XPATH, "//*[@id='menuUserLink']")
    By_sign_out = (By.XPATH, "//*[@id='loginMiniTitle']/label[3]")
    #objects in mobile user menu
    By_user_menu_m = (By.ID, "mobileUser")
    By_sign_out_m = (By.XPATH, "//*[@id='loginMobileMiniTitle']/label[3]")
    By_user_menu_m_indicator = (By.XPATH, "//*[@id='mobile-section']/ul/li[3]/a/span")
    #page load object
    By_load_screen = (By.XPATH, "/html/body/div[2]")



class AO_Nav_Objects(object):
    By_mobile_dropdown = (By.ID, "mobile-btn")
    By_user_menu = (By.XPATH, "//*[@id='menuUserLink']")
    By_user_menu_m = (By.ID, "mobileUser")
    #dependent on user menu
    By_account_link = (By.XPATH, "//*[@id='loginMiniTitle']/label[1]")
    By_account_link_m = (By.XPATH, "//*[@id='loginMobileMiniTitle']/label[1]")
    By_account_indicator = (By.XPATH, "//*[@id='myAccountContainer']")
    By_orders_link = (By.XPATH, "//*[@id='loginMiniTitle']/label[2]")
    By_orders_link_m = (By.XPATH, "//*[@id='loginMobileMiniTitle']/label[2]")
    By_orders_indicator = (By.CLASS_NAME, "myOrderSection")
    #
    By_shopping_cart_link = (By.XPATH, "//*[@id='shoppingCartLink']")
    By_shopping_cart_link_m = (By.ID, "mobileCart")
    By_shopping_cart_indicator = (By.XPATH, "//*[@id='shoppingCart']")
    #
    By_about_dropdown = (By.XPATH, "//*[@id='helpLink']")
    By_about_link = (By.XPATH, "//*[@id='helpMiniTitle']/label[1]")
    By_about_indicator = (By.XPATH, "//*[@id='aboutPage']")
    By_aos_link = (By.XPATH, "//*[@id='helpMiniTitle']/label[2]")
    By_aos_indicator = (By.XPATH, "//*[@id='versionSection']")
    #shop links
    By_speakers_link = (By.XPATH, "//*[@id='speakersImg']")
    By_speakers_indicator = (By.XPATH, "/html/body/div[3]/section/article/div[2]/nav/a[2]")
    
