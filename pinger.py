from bs4 import BeautifulSoup
from html.parser import HTMLParser
from time import localtime
from simpleaudio import WaveObject
from requests import get
from json import dumps, load
from threading import Thread, active_count



def play_sound(sound_file):
    try:
        audio_object = WaveObject.from_wave_file(f"./sounds/{sound_file}")
        play = audio_object.play()
        play.wait_done()
        play.stop()
    except FileNotFoundError:
        print(f"{sound_file} file not found.")
    except Exception:
        print("Error with playing notification audio.")
    finally:
        return

def html_request(url):
    try:
        new_request = get(url)
    except Exception:
        print ("Error making HTTP request")
        return False
    else:
        return BeautifulSoup(new_request.text, "html.parser")

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

#Halts program for configured time before making another request
def wait():
    global continue_condition
    for timer in range(config.interval):
        if continue_condition:
            sleep(1)
        else:
            break

def get_product_name(url):
    html_object = html_request(url)
    if not (html_object):
        return
    html_object = BeautifulSoup(html_object.text, "html.parser")
    product_name = html_object.find_all("h1", class_="productName_2KoPa")
    return product_name.string

def best_buy_in_stock(html_object):
    global in_stock_dict
    pass

def amazon_in_stock(html_object):
    global in_stock_dict
    pass

def memory_express_in_stock(html_object):
    global in_stock_dict
    pass

def canada_computers_in_stock(html_object):
    global in_stock_dict
    pass

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

def looper():
    global continue_condition
    while continue_condition:
        config.load_config()
        checker()
        wait()

#start application
def start():
    if (active_count() > 1):
        print("Checker already running. \n")
        return
    print ("Starting checker \n")
    global continue_condition
    continue_condition = True
    process = Thread(target=looper)
    process.start()

#stop application
def stop():
    if (active_count() == 1):
        print ("Checker not running.\n")
        return
    print ("Stopping checker.\n")
    global continue_condition
    continue_condition = False

def main():
    command_dict = {"instock": print_in_stock,
                    "new": config.add_product,
                    "del": config.delete_product,
                    "help": print_manual,
                    "fresh": config_reset,
                    "start": start,
                    "stop": stop}

    while True:
        print ("-------------------------")
        user_input = input()
        print ("-------------------------")
        if (user_input in command_dict.keys()):
            command_dict[user_input]()
        elif (user_input == "exit"):
            stop()
            print("Program exiting.")
            break
        elif (user_input == ""):
            print ("")
        else:
            print ("Unknown command.")


if __name__ == '__main__':
    global in_stock_dict
    global continue_condition
    config = Config()
    in_stock_dict = dict()
    config.load_config()
    main()
