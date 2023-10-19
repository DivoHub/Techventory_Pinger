from requests import get
from bs4 import BeautifulSoup


def best_buy_scraper(url):
    best_buy_in_stock(html_object)
    try:
        html_object = html_object.find("span", class_="availabilityMessage_3ZSBM container_1DAvI")
    except Exception:
        html_object = html_object.find("span", class_="availabilityMessageTitle_3FLAg")
    if (html_object.string == "Available to ship"):
        print (f"Item in stock")
        return True
    else:
        return False
        play_sound("instock.mp3")
        in_stock_list.append()

def amazon_scraper(url):
    try:
        price = html_object.find("span", class_="a-offscreen").string
    except Exception:
        return False
    else:
        return price


def memory_express_scraper(url):
    try:
        html_object = html_object.find("span", class_="c-capr-inventory-store__availability InventoryState_OutOfStock")
    except Exception:
        html_object = html_object.find("span", class_="c-capr-inventory-store__availability InventoryState_InStock")
    if (html_object.string == "Out of Stock"):
        return False
    else:
        return True


def canada_computers_scraper():
    try:
        html_object = html_object.find("span", id_="storeinfo")
    except Exception:
        html_object = html_object.find("span", class_="storeinfo mb-1")
    if ("sold out" in html_object.string.casefold()):
        return False
    elif ("available" in html_object.string.casefold()):
        return True
    else:
        return None

def newegg_scraper():
    try:
        html_object = html_object.find("div", class_="product-inventory")
        html_object = html_object.find_all("strong")
    except Exception:
        return False
    if (html_object == "In Stock"):
        return True

def newegg_scraper():
    try:
        html_object = html_object.find("div", class_="product-inventory")
        html_object = html_object.find_all("strong")
    except Exception:
        return False
    if (html_object == "In Stock"):
        return True

def vuugo_checker():
    try:
        html_object = html_object.find("div", id="product-availability")
        html_object = html_object.find_all("span")
    except Exception:
        return False
    if (html_object == "In Stock"):
        return True


def website_director(user_input):
    if ("bestbuy" in user_input):
        best_buy_checker()
    elif ("memoryexpress" in user_input):
        memory_express_checker()
    elif ("canadacomputers" in user_input):
        canada_computers_checker()
    elif ("newegg" in user_input):
        newegg_checker()
    else:
        print ("Unrecognized site or input.")
        return


def request_beautify(link):
    try:
        html_object = get(link)
    except Exception:
        print ("Error with connection.")
    else:
        return BeautifulSoup(html_object.text, "html.parser")


#check if site returns a 200 status code
def site_is_valid(website_input):
    if (len(website_input) == 0 or not "www." in website_input):
        print ("Invalid website given.")
        return False
    try:
        status_code = get(website_input).status_code
        if (status_code >= 200 and status_code <= 299):
            return True
        elif (status_code == 404):
            print("Invalid Server entered.")
            return False
        else:
            print("Connection error")
            return False
    except Exception:
        return False

