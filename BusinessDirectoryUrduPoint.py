# url https://www.urdupoint.com/business/directory.html
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Chrome("chromedriver.exe")
driver.minimize_window()
import pandas as pd
# the url of the Given site

weburl = "https://www.urdupoint.com/business/directory.html"
driver.get(weburl)
r = requests.get(weburl)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, "html.parser")
data = soup.find_all("i",{"class":"fa fa-briefcase mr5"})
data  = [i.text for i in data]
print(data)
# for a in soup.find_all('a', {'class':"cat_style"}):
#     print ("Found the URL:", a['href'])
# print(data)


companies = [
"Advertising & Marketing","Agriculture","Clothing & Fashion","Associations and NGOs","Automobiles & Vehicles","Banking & Financing",
    "Books, Publications & Libraries",
    "Building Materials","Business Services Provider","Dyes & Chemicals","Commodities & Merchandiser","Computers & IT",
    "Construction & Real Estate","Consultants & Advisers","Designers & Decorators","Detergents & Soaps","Education & Training Centre",
    "Electronics & Electrical Products",
    "Engineering Section","Events Planner","Food & Beverage Products","Fruits & Vegetable Products","Furniture & Wood Products",
    "Handicrafts","Health and Medical","Hotels, Clubs & Food Parlors","Insurance Companies","Jewelers","Leather and Tanneries",
    "Metals, Minerals & Mining","Miscellaneous","Oil, Gas & Fuel","Plastics & Polymers","Postal & Courier Services","Printing & Publishing",
    "Professional Services","Security & Safety","Stone & Marble","Telecommunication","Textiles","Tourism & Travel Agent",
    "Hardware & Tools","Packaging & Paper","Photography","Power & Generators","Water & Water Purification","Petroleum & Products",
    "Architects & Planners","Footwear Products & Services","Transport & Logistics","Public Limited Companies","Rice","Energy & Utilities Products",
    "Radio, TV & Multimedia","Environmental Services","Personal Care & Fitness Centre","Food Processing Machinery","Geo Equipment & Services",
    "Gifts Shops & Toys","Glass, Earthenware & Clay","Home Appliances & Accessories","Home Supplies","Office Equipments & Supplies","Pipes & Fittings",
    "Road Safety & Traffic","Shipping Companies","Sports & Games","Government Sector","Cutlery","Call Centre's","Fun, Entertainment & Hobbies",
    "Horticulture & Gardening","Paints & Varnishes","Pest Control Products & Services","Religion & Belief","Shares & Stock Brokers","Social Services",
    "Watches & Clocks","Poultry","Hair Products & Services",
    "Herbs & Others","Embroidery & Crafts Textile","Batteries","Chains","Industrial Safety Equipment","Sugar Mill Machinery & Parts",
    "Photocopy","Mobile Phones","Knitting","Wool","Cultures","Bakers, Sweets & Confectioners","Baby Products","Packing and Crating",
]
step1_items = []
for i in companies:

    driverirl = driver.get(weburl)
    driver.find_element(By.LINK_TEXT, f"{i.strip()}").click()

    # find subpages 1
    r = requests.get(driver.current_url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    x=soup.find("div",attrs={"id":"list_items"})
    step1_items.append([i.text for i in x])
    # print(step1_items[0])
    for i in step1_items[0]:
        print(i)
        print("url in step1")
        print(driver.current_url)
    #     # print("abc",i)
        driver.find_element(By.LINK_TEXT,i).click()
    #     print(driver.current_url)



    driver.get(weburl)
