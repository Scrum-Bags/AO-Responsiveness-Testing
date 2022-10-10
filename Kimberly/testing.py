
# # var = {
# #     "foo" : "Bar",
# #     "puppy": {
# #         "Cat":"Dog",
# #         "Bee":"Kitty"
# #     }

# # }

# # var2 = {
# #     "Foo":"Bar",
# #     1:3,
# #     "Juice":7,
# #     "Help":["Freddy", "Foxy"],
# #     "Sandwiches":{
# #         "Bread":"White",
# #         "Jellies": "Strawberry",
# #         "Price": 4.99
# #     },
# #     "person":{
# #         "male":{
# #             "pet":"dogies",
# #         },
# #         "female":{
# #             "pet":"kat",
# #         }
# #     }
# # }


# # print (var2["person"])

# # #print ("'{Cat}'".format(**var["puppy"]))
# # #print("{Cat}".format(**var["puppy"]))
# # print("Bread = '{Bread}', Jellies = '{Jellies}', Price = '${Price}'".format(**var2['Sandwiches']))
# # #print("Male = '{pet}'".format(**var2['person']["male"]))
# # # print(var2)
# # # print(var2.items())
# # # var2["Juice"] = "3"
# # # print(var2)
# # #print(var2["Foo"])
# # # print(var2.keys())
# # # print(var2.values())

# # # var["Candy"]="cat"
# # # var2.update(var)
# # # print(var2)

# # # del var2[1]
# # # print(var2)

# # # mystr = "Hello"
# # # print(str(mystr))

# # from datetime import datetime


# # now = datetime.now()

# # current_time = now.strftime("%Y%m%d_%H%M%S")
# # print(current_time)

# import openpyxl

# wb = openpyxl.load_workbook("C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/TestCasesExcel.xlsx")
# wslogin = wb["BrowseStore"]

# print(wslogin.cell(row = 2, column = 1).value)
# print(wslogin.cell(row = 2, column = 2).value)
# print(wslogin.cell(row = 3, column = 2).value)
# print(wslogin.cell(row = 3, column = 1).value)


# # from TestSuiteReporter import TestSuiteReporter
# # from singleton import singleton

# # s = singleton(TestSuiteReporter("AutomationPractice", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")
# # )
# # print(s)
# # if not s.reporter:
# #     print("Hree")
# #     s.reporter = TestSuiteReporter("AutomationPractice", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")

# # print(s.reporter is None)
# # print(s.reporter)

# s = "+59"
# if s.startswith('+'):
#     print (s[1:]+" tippie")
# elif s.startswith('-'):
#     print(s[1:]+" tappon")
# else :
#     print("nopo")

# import random


# i = random.randint(1,10)

# for x in range(i):
#     print("Howdy")



# l = list(range(0,10))

# for x in range(0,5):
#     print(l[x])

# pets = ["Dogs", "Cats", "Bird"]

# box = "Ghost"
# pop = "Goes the weasle"

# print(f"whats with the {box};")

# password = "CoolGuy"

# p = ""
# for i in password:
#     p += "*"

# import sys
# sys.path.insert(1, "Poc\CommonFunctions.py")

# from Poc.CommonFunctions import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from TestSuiteReporter import TestSuiteReporter
# reporter = TestSuiteReporter("Testing", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Reports/", "Kimberly Modeste")

# TCRN = "Jay"
# browser = webdriver.Chrome()
# browser.get('http://automationpractice.com/index.php')


# reporter.addTestCase(TCRN, "TC001","Helosjdas=00v98u3qj")

# reporter[TCRN].reportEvent(eventDescription="Teesting tsr", warning=Warning, 
# dataString="Henno", screenshotCallback=browser.find_element(by=By.ID, value='page').screenshot, 
# imagePath=f"C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/.screenshots/{TCRN}/TestScript{time()}", imageEmbed=False)

# # "C:\Users\OWNER\OneDrive\Documents\UFTOne\tests\selenium\Test\.screenshots\TestingImg\TestScript20220928_191634.png"
# # "C:\Users\OWNER\OneDrive\Documents\UFTOne\tests\selenium\Test\Reports/.screenshots/TestingImg/TestScript20220928_191634.png"
# browser.close()

# def s (w, h):
#     print(f"W: {w}, H:{h}")

# def k ():
#     return {9, 6}

# s(*k())

# foo = {"bar", "car"}

# f = foo.pop()
# g = foo.pop()
# print(f)

# bar = ("Carry", "Me", "Home")
# print(bar[0] )

# from datetime import datetime
# from typing import Type


# s = 400,000,00

# if type(s) == str:
#     print("is string")
# elif type(s) == datetime:
#     print("is date")
# elif type(s) == int:
#     print("is int")


import time

print("Hi")
time.sleep(5)
print("Loading", end="")
for x in range(5):
    print(".", end= "")
    time.sleep(1)
print("")



print("Hello")