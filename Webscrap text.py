from selenium import webdriver

#change the selenium broswer's language to english
from selenium.webdriver.chrome.options import Options
browser_locale = 'en-ca'
chrome_driver_path = 'C:/Users/XX/XXX/chromedriver.exe'
options = Options()
options.add_argument("--lang={}".format(browser_locale))

webbrowser = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

import requests
import pandas as pd
count=0
nonPriceProducts=[]

df0 = pd.read_excel('productIDList.xlsx')
productID = df0['productID']

#productID=['B0002EBI82','B0002MPS7G', 'B00080DK86', 'B000PH8KDW', 'B000ULGO7M','B0002MPS7G','B00080DK86', 'B000BK1U5S', 'B000C1VYDY',]
#productID=['B0002MPS7G']
productPriceList=[]
for id in productID:
    webbrowser.get('https://www.amazon.com/dp/'+id)
    try:
        element = webbrowser.find_element_by_xpath('//*[@id="priceblock_ourprice"]')
        element2 = webbrowser.find_element_by_xpath('//*[@id="productTitle"]')
        if element.text:
            productPrice = {}
            productPrice['productID']=id
            productPrice['price'] = element.text
            productPrice['name'] = element2.text
            productPriceList.append(productPrice)
        else:
            continue
    except:
        nonPriceProducts.append(id)
        count += 1

df = pd.DataFrame(productPriceList)

with pd.ExcelWriter('productPrice.xlsx') as writer:
    df.to_excel(writer)

with open('nonPriceProducts.txt', 'w') as f:
    print('file is open')
    f.write('total number of non price products is ' + str(count))
    f.write('\n')
    f.write(str(nonPriceProducts))

print(f'total number of non price products is {count}')
