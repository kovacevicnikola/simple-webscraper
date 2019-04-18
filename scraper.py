from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url= 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'


uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})


filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    a = container.findAll("a", {"class":"item-brand"})
    a = a[0]
    brand = a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()


    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
