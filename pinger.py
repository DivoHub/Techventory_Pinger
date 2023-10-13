from bs4 import BeautifulSoup
from html.parser import HTMLParser
from time import localtime
from requests import get
from json import dumps, load
from threading import Thread, active_count




#Prints help manual to console
def print_manual():
    manual = open('help.txt', 'r')
    print (manual.read())
    manual.close()


def html_request(url):
    try:
        new_request = get(url)
    except Exception:
        print ("Error making HTTP request")
        return False
    else:
        return BeautifulSoup(new_request.text, "html.parser")

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

#Halts program for configured time before making another request
def wait():
    for timer in range(config.interval):
        if continue_condition:
            sleep(1)
        else:
            break

#returns string containing the title of the part given by website / makes HTTP request
def get_product_name(url):
    html_object = html_request(url)
    if not (html_object):
        return
    html_object = BeautifulSoup(html_object.text, "html.parser")
    product_name = html_object.find_all("h1", class_="productName_2KoPa")
    return product_name.string

def best_buy_in_stock(html_object):
    pass

def amazon_in_stock(html_object):
    try:
        int(html_object.find("span", class_="a-offscreen").string)
    except Exception:
        return False
    else:
        return True

def memory_express_in_stock(html_object):
    pass

def canada_computers_in_stock(html_object):
    pass

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
    config = Config()
    in_stock_dict = dict()
    config.load_config()
    main()
