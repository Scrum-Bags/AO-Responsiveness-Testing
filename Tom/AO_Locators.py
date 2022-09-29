from selenium.webdriver.common.by import By

class BasePageLocators(object):
    By_shopping_cart_link = (By.ID, 'shoppingCartLink')
    By_username = (By.XPATH, '/html/body/header/nav/ul/li[3]/a/span')
    By_shopping_cart_num = (By.XPATH, '/html/body/header/nav/ul/li[2]/a/span')

class HomePageLocators(object):
    By_speakers_link = (By.ID, 'speakersTxt')
    By_laptops_link = (By.ID, 'laptopsTxt')
    By_tablets_link = (By.ID, 'tabletsTxt')
    By_mice_link = (By.ID, 'miceTxt')
    By_headphones_link = (By.ID, 'headphonesTxt')
    By_user_btn = (By.ID, 'menuUser')

    #only loaded when login box is open
    By_username_field = (By.NAME, 'username')
    By_password_field = (By.NAME, 'password')
    By_signin_btn = (By.ID, 'sign_in_btnundefined')

class StorePageLocators(object):
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')
    By_clear_selection = (By.XPATH, '//*[@id="mobileSlide"]/label/label')
    By_num_items = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[1]/p/a')
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_price_left_val = (By.XPATH, '//*[@id="mobileSlide"]/ul/li[1]/div/p[1]')
    By_price_right_val = (By.XPATH, '//*[@id="mobileSlide"]/ul/li[1]/div/p[2]')
    By_price_slider = (By.XPATH, '//*[@id="slider"]/div/div[1]')
    By_responsive_filter = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[1]/p/span')
    By_mobile_slider = (By.ID, 'mobileSlide')

class SpeakersPageLocators(object):
    #Expanders and price slider
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_compatibility_expander = (By.ID, 'accordionAttrib0')
    By_manufacturer_expander = (By.ID, 'accordionAttrib1')
    By_weight_expander = (By.ID, 'accordionAttrib2')
    By_wireless_expander = (By.ID, 'accordionAttrib3')
    By_color_expander = (By.ID, 'accordionColor')
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')

    #Individual option boxes (need to have expander open to access)
    By_compat_0 = (By.NAME, 'compatibility_0')
    By_compat_1 = (By.NAME, 'compatibility_1')
    By_manufacturer_0 = (By.NAME, 'manufacturer_0')
    By_manufacturer_1 = (By.NAME, 'manufacturer_1')
    By_manufacturer_2 = (By.NAME, 'manufacturer_2')
    By_weight_0 = (By.NAME, 'weight_0')
    By_weight_1 = (By.NAME, 'weight_1')
    By_weight_2 = (By.NAME, 'weight_2')
    By_weight_3 = (By.NAME, 'weight_3')
    By_weight_4 = (By.NAME, 'weight_4')
    By_weight_5 = (By.NAME, 'weight_5')
    By_weight_6 = (By.NAME, 'weight_6')
    By_wireless_0 = (By.NAME, 'wireless_technology_0')
    By_wireless_1 = (By.NAME, 'wireless_technology_1')
    By_color_BLACK = (By.ID, 'productsColors414141')
    By_color_BLUE = (By.ID, 'productsColors3683D1')
    By_color_GRAY = (By.ID, 'productsColorsC3C3C3')
    By_color_PURPLE = (By.ID, 'productsColors545195')
    By_color_RED = (By.ID, 'productsColorsDD3A5B')
    By_color_TURQUOISE = (By.ID, 'productsColors55CDD5')
    By_color_WHITE = (By.ID, 'productsColorsFFFFFF')
    By_color_YELLOW = (By.ID, 'productsColorsFCC23D')

class LaptopsPageLocators(object):
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_display_expander = (By.ID, 'accordionAttrib0')
    By_os_expander = (By.ID, 'accordionAttrib1')
    By_processor_expander = (By.ID, 'accordionAttrib2')
    By_weight_expander = (By.ID, 'accordionAttrib3')
    By_color_expander = (By.ID, 'accordionColor')
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')

    #Individual option boxes (need to have expander open to access)
    By_display_0 = (By.NAME, 'display_0')
    By_display_1 = (By.NAME, 'display_1')
    By_display_2 = (By.NAME, 'display_2')
    By_display_3 = (By.NAME, 'display_3')
    By_display_4 = (By.NAME, 'display_4')
    By_display_5 = (By.NAME, 'display_5')
    By_display_6 = (By.NAME, 'display_6')
    By_display_7 = (By.NAME, 'display_7')
    By_display_8 = (By.NAME, 'display_8')
    By_display_9 = (By.NAME, 'display_9')
    By_display_10 = (By.NAME, 'display_10')
    By_os_0 = (By.NAME, 'operating_system_0')
    By_os_1 = (By.NAME, 'operating_system_1')
    By_os_2 = (By.NAME, 'operating_system_2')
    By_os_3 = (By.NAME, 'operating_system_3')
    By_processor_0 = (By.NAME, 'processor_0')
    By_processor_1 = (By.NAME, 'processor_1')
    By_processor_2 = (By.NAME, 'processor_2')
    By_processor_3 = (By.NAME, 'processor_3')
    By_processor_4 = (By.NAME, 'processor_4')
    By_processor_5 = (By.NAME, 'processor_5')
    By_processor_6 = (By.NAME, 'processor_6')
    By_processor_7 = (By.NAME, 'processor_7')
    By_processor_8 = (By.NAME, 'processor_8')
    By_processor_9 = (By.NAME, 'processor_9')
    By_weight_0 = (By.NAME, 'weight_0')
    By_weight_1 = (By.NAME, 'weight_1')
    By_weight_2 = (By.NAME, 'weight_2')
    By_weight_3 = (By.NAME, 'weight_3')
    By_weight_4 = (By.NAME, 'weight_4')
    By_weight_5 = (By.NAME, 'weight_5')
    By_weight_6 = (By.NAME, 'weight_6')
    By_weight_7 = (By.NAME, 'weight_7')
    By_weight_8 = (By.NAME, 'weight_8')
    By_weight_9 = (By.NAME, 'weight_9')
    By_weight_10 = (By.NAME, 'weight_10')
    By_color_BLACK = (By.ID, 'productsColors414141')
    By_color_BLUE = (By.ID, 'productsColors3683D1')
    By_color_GRAY = (By.ID, 'productsColorsC3C3C3')
    By_color_PURPLE = (By.ID, 'productsColors545195')
    By_color_RED = (By.ID, 'productsColorsDD3A5B')
    By_color_TURQUOISE = (By.ID, 'productsColors55CDD5')
    By_color_WHITE = (By.ID, 'productsColorsFFFFFF')
    By_color_YELLOW = (By.ID, 'productsColorsFCC23D')

class TabletsPageLocators(object):
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_display_expander = (By.ID, 'accordionAttrib0')
    By_processor_expander = (By.ID, 'accordionAttrib1')
    By_color_expander = (By.ID, 'accordionColor')
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')

    #Individual option boxes (need to have expander open to access)
    By_display_0 = (By.NAME, 'display_0')
    By_display_1 = (By.NAME, 'display_1')
    By_display_2 = (By.NAME, 'display_2')
    By_processor_0 = (By.NAME, 'processor_0')
    By_processor_1 = (By.NAME, 'processor_1')
    By_processor_2 = (By.NAME, 'processor_2')
    By_color_BLACK = (By.ID, 'productsColors414141')
    By_color_GRAY = (By.ID, 'productsColorsC3C3C3')

class MicePageLocators(object):
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_scroller_expander = (By.ID, 'accordionAttrib0')
    By_color_expander = (By.ID, 'accordionColor')
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')

    #Individual option boxes (need to have expander open to access)
    By_scroller_0 = (By.NAME, 'scroller_type_0')
    By_scroller_1 = (By.NAME, 'scroller_type_1')
    By_scroller_2 = (By.NAME, 'scroller_type_2')
    By_scroller_3 = (By.NAME, 'scroller_type_3')
    By_scroller_4 = (By.NAME, 'scroller_type_4')
    By_color_BLACK = (By.ID, 'productsColors414141')
    By_color_BLUE = (By.ID, 'productsColors3683D1')
    By_color_GRAY = (By.ID, 'productsColorsC3C3C3')
    By_color_PURPLE = (By.ID, 'productsColors545195')
    By_color_RED = (By.ID, 'productsColorsDD3A5B')
    By_color_WHITE = (By.ID, 'productsColorsFFFFFF')

class HeadphonesPageLocators(object):
    By_price_expander = (By.ID, 'accordionPrice')
    By_price_left_handle = (By.XPATH,'//*[@id="slider"]/div/div[1]/div')
    By_price_right_handle = (By.XPATH, '//*[@id="slider"]/div/div[2]/div')
    By_compatibility_expander = (By.ID, 'accordionAttrib0')
    By_connector_expander = (By.ID, 'accordionAttrib1')
    By_weight_expander = (By.ID, 'accordionAttrib2')
    By_color_expander = (By.ID, 'accordionColor')
    By_item_area = (By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li')

    #Individual option boxes (need to have expander open to access)
    By_compat_0 = (By.NAME, 'compatibility_0')
    By_compat_1 = (By.NAME, 'compatibility_1')
    By_compat_2 = (By.NAME, 'compatibility_2')
    By_connector_0 = (By.NAME, 'connector_0')
    By_connector_1 = (By.NAME, 'connector_1')
    By_weight_0 = (By.NAME, 'weight_0')
    By_weight_1 = (By.NAME, 'weight_1')
    By_weight_2 = (By.NAME, 'weight_2')
    By_weight_3 = (By.NAME, 'weight_3')
    By_color_BLACK = (By.ID, 'productsColors414141')
    By_color_BLUE = (By.ID, 'productsColors3683D1')
    By_color_GRAY = (By.ID, 'productsColorsC3C3C3')
    By_color_PURPLE = (By.ID, 'productsColors545195')
    By_color_RED = (By.ID, 'productsColorsDD3A5B')
    By_color_TURQUOISE = (By.ID, 'productsColors55CDD5')
    By_color_WHITE = (By.ID, 'productsColorsFFFFFF')
    By_color_YELLOW = (By.ID, 'productsColorsFCC23D')

class ItemPageLocators(object):
    By_minus_btn = (By.CLASS_NAME, 'minus')
    By_plus_btn = (By.CLASS_NAME, 'plus')
    By_add_to_cart_btn = (By.NAME, 'save_to_cart')
    By_color_select = (By.XPATH, '/html/body/div[3]/section/article[1]/div[2]/div[2]/div/div[1]/div[2]/span') #needs a number specified at end
    By_item_name = (By.XPATH, '/html/body/div[3]/section/article[1]/div[2]/div[2]/h1')
    By_item_price = (By.XPATH, '/html/body/div[3]/section/article[1]/div[2]/div[2]/h2')

class ShoppingCartPageLocators(object):
    By_checkout_btn = (By.ID, 'checkOutButton')
    By_edit_btn = (By.XPATH, '//*[@id="shoppingCart"]/table/tbody/tr/td[6]/span/a[1]')
    By_remove_btn = (By.XPATH, '//*[@id="shoppingCart"]/table/tbody/tr/td[6]/span/a[3]')

class OrderPaymentPageLocators(object):
    #page 1
    By_edit_shipping_link = (By.XPATH, '//*[@id="userSection"]/div[1]/div[2]/a')
    By_next_btn = (By.ID, 'next_btn')

    #page 2
    By_safepay_method = (By.NAME, 'safepay')
    By_mastercredit_method = (By.NAME, 'masterCredit')
    #safepay details
    By_safepay_user = (By.NAME, 'safepay_username')
    By_safepay_password = (By.NAME, 'safepay_password')
    By_safepay_paynow = (By.ID, 'pay_now_btn_SAFEPAY')
    #mastercredit details (must have mastercredit selected to load)
    By_card_num = (By.ID, 'creditCard')
    By_cvv_num = (By.NAME, 'cvv_number')
    By_expiration_mm = (By.NAME, 'mmListbox')
    By_expiration_yyyy = (By.NAME, 'yyyyListbox')
    By_cardholder_name = (By.NAME, 'cardholder_name')
    By_creditcard_paynow = (By.NAME, 'pay_now_btn_MasterCredit')

class OrderConfirmationPageLocators(object):
    By_tracking_num = (By.ID, 'trackingNumberLabel')
    By_order_num = (By.ID, 'orderNumberLabel')
    By_order_total = (By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[3]/div[3]/label/a')

class OrderHistoryPageLocators(object):
    By_order_num = (By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr[2]/td[1]/label')
    By_total_price = (By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr[2]/td[7]/label')