from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# url from which i would like to scrap my data
myUrl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=Graphics%20card"


'''OPENING THE CONNECTION, GRABBING THE PAGE'''

# open the website and grap inside my script
openMyUrl = uReq(myUrl)

# Now i would like to read from my graped site
page_html = openMyUrl.read()

# As it is open connection i need to grab it
openMyUrl.close()

'''HTML PARSING'''

# parse html
page_soup = soup(page_html,'html.parser')
print(page_soup.h1)


#Make CSV file for wrapped data
filename="Product.csv"
f=open(filename,'w')
header = "Brands, Product Name, Shipping details\n"
f.write(header)

# Grab all product
containers = page_soup.find_all("div",{"class":"item-container"})
print("Number of product contained in this webpage:: ",len(containers))

for contains in containers:
    try:
        brand = contains.div.div.a.img['title']

        product_name_container = contains.find_all('a',{'class':'item-title'})
        product_name=product_name_container[0].text

        shipping_container=contains.find_all('li',{'class':'price-ship'})
        shipping_details=shipping_container[0].text.strip()

        print("Brand:: ", brand)
        print("Product Name:: ",product_name)
        print("Shipping Price:: ",shipping_details)

        f.write(brand+ ","+ product_name.replace(",","") +","+shipping_details +"\n")


    except:
        print("NOPE"," ","NOPE")
        pass
    print('\n\n')

f.close()