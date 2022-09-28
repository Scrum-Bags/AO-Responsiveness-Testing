"""Storage for Advantage Online object identifiers."""

from selenium.webdriver.common.by import By


commonElementIDs = {
    "user_icon": {
        "by": By.ID,
        "value": "menuUser"
    },
    "loader": {
        "by": By.CLASS_NAME,
        "value": "loader"
    }
}

commonMobileElementIDs = {
    "mobile_sidebar_button": {
        "by": By.ID,
        "value": "mobile-btn"
    },
    "mobile_home": {
        "by": By.ID,
        "value": "mobileHome"
    },
    "mobile_cart": {
        "by": By.ID,
        "value": "mobileCart"
    },
    "mobile_user": {
        "by": By.ID,
        "value": "mobileUser"
    }
}
# Note: mobile UI kicks in when pagewidth < 464px

mainPageWideElementIDs = {
    "jump_links": {
        "by": By.CLASS_NAME,
        "value": "nav-li-links"
    },
    "search_icon": {
        "by": By.ID,
        "value": "menuSearch"
    },
    "offer_button": {
        "by": By.ID,
        "value": "see_offer_btn"
    }
}

mainPageWaitIDs = {
    "speakers_image": {
        "by": By.ID,
        "value": "speakersImg"
    },
    "tablets_image": {
        "by": By.ID,
        "value": "tabletsImg"
    },
    "laptops_image": {
        "by": By.ID,
        "value": "laptopsImg"
    },
    "mice_image": {
        "by": By.ID,
        "value": "miceImg"
    },
    "headphones_image": {
        "by": By.ID,
        "value": "headphonesImg"
    }
}

loggedOutCommonElementIDs = {
    "new_account": {
        "by": By.CLASS_NAME,
        "value": "create-new-account"
    }
}

loggedInCommonElementIDs = {
    "user_menu": {
        "by": By.ID,
        "value": "menuUserLink"
    },
    "menu_items_container": {
        "by": By.ID,
        "value": "loginMiniTitle"
    }
}

userRegisterElementIDs = {
    "username": {
        "by": By.NAME,
        "value": "usernameRegisterPage"
    },
    "username_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[1]/div[1]/sec-view[1]/div/label"
    },
    "email": {
        "by": By.NAME,
        "value": "emailRegisterPage"
    },
    "email_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[1]/div[1]/sec-view[2]/div/label"
    },
    "password": {
        "by": By.NAME,
        "value": "passwordRegisterPage"
    },
    "password_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[1]/div[2]/sec-view[1]/div/label"
    },
    "password_confirm": {
        "by": By.NAME,
        "value": "confirm_passwordRegisterPage"
    },
    "password_confirm_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[1]/div[2]/sec-view[2]/div/label"
    },
    "first_name": {
        "by": By.NAME,
        "value": "first_nameRegisterPage"
    },
    "first_name_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[2]/div[1]/sec-view[1]/div/label"
    },
    "last_name": {
        "by": By.NAME,
        "value": "last_nameRegisterPage"
    },
    "last_name_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[2]/div[1]/sec-view[2]/div/label"
    },
    "phone_number": {
        "by": By.NAME,
        "value": "phone_numberRegisterPage"
    },
    "phone_number_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[2]/div[2]/sec-view/div/label"
    },
    "address_country": {
        "by": By.NAME,
        "value": "countryListboxRegisterPage"
    },
    "address_city": {
        "by": By.NAME,
        "value": "cityRegisterPage"
    },
    "address_city_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[3]/div[1]/sec-view[2]/div/label"
    },
    "address_street": {
        "by": By.NAME,
        "value": "addressRegisterPage"
    },
    "address_street_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[3]/div[2]/sec-view[1]/div/label"
    },
    "address_region": {
        "by": By.NAME,
        "value": "state_/_province_/_regionRegisterPage"
    },
    "address_region_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[3]/div[2]/sec-view[2]/div/label"
    },
    "address_postal_code": {
        "by": By.NAME,
        "value": "postal_codeRegisterPage"
    },
    "address_postal_code_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[1]/div[2]/div/div[3]/div[3]/sec-view/div/label"
    },
    "offers_opt_in": {
        "by": By.NAME,
        "value": "allowOffersPromotion"
    },
    "terms_and_conditions_opt_in": {
        "by": By.NAME,
        "value": "i_agree"
    },
    "register_button": {
        "by": By.ID,
        "value": "register_btnundefined"
    },
    "register_fail_error": {
        "by": By.XPATH,
        "value": "/html/body/div[3]/section/article/sec-form/div[2]/label[1]"
    }  # 'User name already exists '
}

accountSummaryElementIDs = {
    "details_box": {
        "by": By.CLASS_NAME,
        "value": "borderBox"
    }
}