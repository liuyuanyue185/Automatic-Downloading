#open webDriver. ensure you've download it manually in your computer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
import time

startTime= time.time()
#create a folder for scrapped documents
import os

SAVE_FOLDER = 'images'
if not os.path.exists(SAVE_FOLDER):
    os.mkdir(SAVE_FOLDER)

#scrapping and download the images
#use try&except in case some web can not open and record how many and which can not open.
import requests
count=0
nonImageProducts=[]
productID=['B0002EBI82','B0002MPS7G', 'B00080DK86', 'B000PH8KDW', 'B000ULGO7M','B0002MPS7G','B00080DK86', 'B000BK1U5S', 'B000C1VYDY', 'B000NL0T1G']
for id in productID:
    browser.get('https://www.amazon.com/dp/'+id)
    try:
        element = browser.find_element_by_xpath('//*[@id="landingImage"]')
        src = element.get_attribute('src')
        # print(element.get_attribute('src'))
        # browser.get(element.get_attribute('src'))
        response = requests.get(src)
        imagename = SAVE_FOLDER + '/' + id + '.jpg'     #***SAVE_FOLDER here is poiting out the path
        with open(imagename, 'wb') as file:
            file.write(response.content)
    except:
        count += 1
        nonImageProducts.append(id)
        pass

finishedTime = time.time()
#record the performance for futher analysis
with open('products ID without images.txt', 'w') as f:
    print('file is open')
    f.write('total number of non image products is ' + str(count))
    f.write('\n')
    f.write(str(nonImageProducts))
    f.write('\n')
    f.write('total running time is ' + str(finishedTime-startTime))

#self testing, the below could be deleted
print('total number of non image products is ' + str(count))
print('non image products ID ' + str(nonImageProducts))
print(f'total running time is : {finishedTime-startTime}')