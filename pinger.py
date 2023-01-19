from bs4 import BeautifulSoup
from html.parser import HTMLParser
from time import localtime
from simpleaudio import WaveObject

api = BeautifulSoup()


def ping_user():
    pass

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


def memory_express_checker():
    pass




def best_buy_checker():
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


if __name__ == '__main__':