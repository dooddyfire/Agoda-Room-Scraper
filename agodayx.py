import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException


#url = "https://www.agoda.com/jomtien-thani-hotel/hotel/pattaya-th.html?finalPriceView=1&isShowMobileAppPrice=false&cid=-999&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-06-3&isCalendarCallout=false&childAges=8&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=THB&isFreeOccSearch=false&isCityHaveAsq=true&los=1&searchrequestid=8600e906-ed85-45d5-be65-91f1b9f62b94"

url = input("Enter agoda url : ")
#Get bot selenium make sure you can access google chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')

check_in = soup.find('div',{'data-selenium':'checkInBox'}).text
check_out = soup.find('div',{'data-selenium':'checkOutBox'}).text


print("check in : {}".format(check_in))
print("check out : {}".format(check_out))

hotel_name = soup.find('p',{'data-selenium':'hotel-header-name'}).text 
print(hotel_name)


prop_desc = soup.find('div',{'data-element-name':'property-short-description'}).text
print(prop_desc)

location = soup.find('div',{'class':'HeaderCerebrum__Location'}).text 
print(location)

room_name = soup.find('span',{'class':'MasterRoom__HotelName'}).text 
print(room_name)

price = soup.find('div',{'class':'StickyNavPrice__priceDetail--lowerText'}).text.replace('from','')
print(price)

df = pd.DataFrame()
df['Hotel Name'] = [hotel_name] 
df['Description'] = [prop_desc]
df['Location'] = [location] 
df['Room Name'] = [room_name] 
df['Check in'] = [check_in] 
df['Check Out'] = [check_out] 
df['Price'] = [price]

df.to_excel('TestAgo.xlsx')