def best_buy_checker(url):
    html_object = html_request(url)
    html_object = BeautifulSoup(html_object.text, "html.parser")
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

def amazon_checker(url):
    global in_stock_dict
    html_object = html_request(url)
    html_object = BeautifulSoup(html_object.text, "html.parser")
    try:
        price = html_object.find("span", class_="a-offscreen").string
    except Exception:
        return False
    else:
        return price


def memory_express_checker(url):
    global in_stock_dict
    html_object = html_request(url)
    html_object = BeautifulSoup(html_object.text, "html.parser")
    try:
        html_object = html_object.find("span", class_="c-capr-inventory-store__availability InventoryState_OutOfStock")
    except Exception:
        html_object = html_object.find("span", class_="c-capr-inventory-store__availability InventoryState_InStock")
    if (html_object.string == "Out of Stock"):
        return False
    else:
        return True


def canada_computers_checker():
    global in_stock_dict
    html_object = html_request(url)
    html_object = BeautifulSoup(html_object.text, "html.parser")
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

def newegg_checker():
    global in_stock_dict
    html_object = html_request()
    html_object = BeautifulSoup(html_object.text, "html.parser")
    try:
        html_object = html_object.find("div", class_="product-inventory")
        html_object = html_object.find_all("strong")
    except Exception:
        return False
    if (html_object == "In Stock"):
        return True

def checker_director(user_input):
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
