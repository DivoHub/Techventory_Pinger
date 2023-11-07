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


def looper():
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
