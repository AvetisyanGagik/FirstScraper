import requests
from bs4 import BeautifulSoup
import json

# url = 'https://ohanyan.am/am/chess/chess.html'
#
#
#
# req = requests.get(url)
# src = req.text
# # print(src)
#
# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src,'lxml')


chess_product_names= soup.find_all(class_ = "product_name combo_link")
prices = soup.find_all(class_ = 'product_price')
product_links = soup.find_all(class_ = 'product_name combo_link')
dict = dict()
for item in range(len(chess_product_names)):
    dict[chess_product_names[item].text] = [prices[item].text.strip(),product_links[item].get('href')]
    # print('CHess', '----', chess_product_names[item].text)
    # print('Prices', '---', prices[item].text.strip())
print(dict)

with open('dictonary.json', 'w') as file:
    json.dump(dict,file, indent = 4, ensure_ascii= False)






