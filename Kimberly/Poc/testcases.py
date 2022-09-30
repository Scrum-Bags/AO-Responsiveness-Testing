testcasevalues = {
    "valid": {
        "title": "User will be attempting to update Personal Information with valid information",
        "login": { 
            "email":"Maximumride567@gmail.com",
            "password":"Kimberly1!"
        },
        "personalInfo" : {
            "gender": 0,
            "fname":"Kreolys",
            "lname":"Sekai",
            "email":"Maximumride567@gmail.com",
            "month": 9,
            "day": 5,
            "year": 1998,
            "opass": "Kimberly1!",
            "newpass": "Kimberly1!",
            "conpass": "Kimberly1!",
            "news": False,
            "opt": False,
        },
        "address":{
            "fname":"Kretos",
            "lname":"Lito",
            "company":"",
            "address1":"163 Usnl Rd.",
            "address2":"",
            "city":"Ziks",
            "state": 39,
            "zipcode":"15628",
            "country": 0,
            "home":"145-550-4523",
            "mobile":"",
            "othertext":"Hi miss Alice, ああなたガラスの。めでどんなゆめを。みられるの？みられるの？またあたし、こころがさけて。ねがれでる。つくろった、すきまにささる。きよくたち。Hi Miss Alice, あなたかじつの。くしでだれにあいを。なげてるの？投げてるの？もうあたし。ことばおつまく、したのねつ。さめきって、めでるおうたうも、うたえない。Still, You do not answer. Still, you do not answer.",
            "alias":"Address",
        }
    },
    "error":{
        "title": "User will be attempting to update Personal Information with invalid information",
        "login": { 
            "email":"Maximumride567@gmail.com",
            "password":"Kimberly1!"
        },
        "personalInfo" : {
            "gender": 0,
            "fname":"Kreolys",
            "lname":"Sekai",
            "email":"ILike@Pancakes",
            "month": 9,
            "day": 5,
            "year": 1998,
            "opass": "Kimberly1!",
            "newpass": "Kimberly1!",
            "conpass": "Kimberly1!",
            "news": False,
            "opt": False,
        },
        "address":{
            "fname":"|3311",
            "lname":"Lito",
            "company":"",
            "address1":"163 Usnl Rd.",
            "address2":"",
            "city":"Ziks",
            "state": 39,
            "zipcode":"15628",
            "country": 0,
            "home":"145-550-4523",
            "mobile":"",
            "othertext":"Hi miss Alice, ああなたガラスの。めでどんなゆめを。みられるの？みられるの？またあたし、こころがさけて。ねがれでる。つくろった、すきまにささる。きよくたち。Hi Miss Alice, あなたかじつの。くしでだれにあいを。なげてるの？投げてるの？もうあたし。ことばおつまく、したのねつ。さめきって、めでるおうたうも、うたえない。Still, You do not answer. Still, you do not answer.",
            "alias":"Address",
        }
    
    }
    
}

testcaseDict = {
    "valid": {
        "loginDict": {
            "description":["User should add the email to form", "User should add passwords to form", "User should press the sign in and be logged in"],
            "expected behavior":["Pass", "Pass", "Pass"],
            "datastring": ["Email: '{email}'".format(**testcasevalues['valid']["login"]), "Password: '{password}'".format(**testcasevalues['valid']["login"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        },
        "personalDict": {
            "description":["User should see gender option picked", "User should see new first name, last name and email", 
                            "User should see new birthday", "User should have old password, (old/new) password added to fields, and confirm password into fields", 
                            "User should not opt into news", "User should not opt in", "User should have submitted all fields successfully"],
            "expected behavior":["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"],
            "datastring": ["Gender: '{gender}'".format(**testcasevalues["valid"]["personalInfo"]),
                "First Name: '{fname}'; Last Name: '{lname}'; Email '{email}'".format(**testcasevalues["valid"]["personalInfo"]),
                "Birthday: '{month}/{day}/{year}'''".format(**testcasevalues["valid"]["personalInfo"]),
                "Old Password: '{opass}'; Password: '{newpass}'; Confirm Password: '{conpass}'".format(**testcasevalues["valid"]["personalInfo"]),
                "Newsletter Opt in: '{news}'".format(**testcasevalues["valid"]["personalInfo"]), 
                "Special Offer Opt in: '{opt}'".format(**testcasevalues["valid"]["personalInfo"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        },
        "addressDict":{
            "description":["User should see new first name and last name", "User should or shouldn't see company name", 
                "User should see the address", "User should see city, state and zipcode", "User should see country", 
                "User should see home or mobile number", "User should end up with a field with both alphabet and kanji", 
                "User should see an alias for the address", "User should submit all fields successfully"],
            "expected behavior":["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "pass"],
            "datastring": ["First Name: '{fname}'; Last Name: '{lname}'".format(**testcasevalues["valid"]["address"]),
                "Company: '{company}'".format(**testcasevalues["valid"]["address"]), 
                "Address 1: '{address1}'; Address 2: '{address2}'".format(**testcasevalues["valid"]["address"]),
                "City: '{city}'; State: '{state}'; Zipcode: '{zipcode}'".format(**testcasevalues["valid"]["address"]),
                "Country: '{country}'".format(**testcasevalues["valid"]["address"]),
                "Home Number: '{home}'; Mobile Number: '{mobile}'".format(**testcasevalues["valid"]["address"]),
                "Other: '{othertext}'".format(**testcasevalues["valid"]["address"]), "Alias: '{alias}'".format(**testcasevalues["valid"]["address"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        }
    },
    "error":{
         "loginDict": {
            "description":["User should add the email to form", "User should add passwords to form", "User should press the sign in and be logged in"],
            "expected behavior":["Pass", "Pass", "Pass"],
            "datastring": ["Email: '{email}'".format(**testcasevalues['error']["login"]), "Password: '{password}'".format(**testcasevalues['error']["login"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        },
         "personalDict": {
            "description":["User should see gender option picked", "User should see new first name, last name and invalid email", 
                            "User should see new birthday", "User should have old password, (old/new) password added to fields, and confirm password into fields", 
                            "User should not opt into news", "User should not opt in", "User should have submitted all fields and there should be an error"],
            "expected behavior":["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Fail"],
            "datastring": ["Gender: '{gender}'".format(**testcasevalues["valid"]["personalInfo"]),
                "First Name: '{fname}'; Last Name: '{lname}'; Email '{email}'".format(**testcasevalues["valid"]["personalInfo"]),
                "Birthday: '{month}/{day}/{year}'''".format(**testcasevalues["valid"]["personalInfo"]),
                "Old Password: '{opass}'; Password: '{newpass}'; Confirm Password: '{conpass}'".format(**testcasevalues["valid"]["personalInfo"]),
                "Newsletter Opt in: '{news}'".format(**testcasevalues["valid"]["personalInfo"]), 
                "Special Offer Opt in: '{opt}'".format(**testcasevalues["valid"]["personalInfo"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        },
        "addressDict":{
            "description":["User should see new invalid first name and valid last name", "User should or shouldn't see company name", 
                "User should see the address", "User should see city, state and zipcode", "User should see country", 
                "User should see home or mobile number", "User should end up with an error with this text", 
                "User should see an alias for the address", "User should submit all fields successfully and error should appear"],
            "expected behavior":["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Fail", "Pass", "Fail"],
            "datastring": ["First Name: '{fname}'; Last Name: '{lname}'".format(**testcasevalues["error"]["address"]),
                "Company: '{company}'".format(**testcasevalues["error"]["address"]), 
                "Address 1: '{address1}'; Address 2: '{address2}'".format(**testcasevalues["error"]["address"]),
                "City: '{city}'; State: '{state}'; Zipcode: '{zipcode}'".format(**testcasevalues["error"]["address"]),
                "Country: '{country}'".format(**testcasevalues["error"]["address"]),
                "Home Number: '{home}'; Mobile Number: '{mobile}'".format(**testcasevalues["error"]["address"]),
                "Other: '{othertext}'".format(**testcasevalues["error"]["address"]), "Alias: '{alias}'".format(**testcasevalues["error"]["address"])],
            "imgStr":"C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/Images/"
        }
    },

}




