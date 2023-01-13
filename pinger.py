from bs4 import BeautifulSoup
from html.parser import HTMLParser
from time import localtime

api = BeautifulSoup()


def ping_user():
    pass




def site_is valid(website_input):
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
    
    
def best_buy_checker():
    pass
def memory_express_checker():
    pass
def canada_computers_checker():
    pass
def newegg_checker():
    pass


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
    
    

def main():
    pass
