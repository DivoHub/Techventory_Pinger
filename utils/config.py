class Config:
    def __init__(self):
        self.links = dict()
        self.interval = 1800
        self.logger_on = False

    def add_product(self):
        while True:
            new_product_url = input("Enter URL to product (enter 'x' when finished):    ")
            if (new_product == 'x'):
                break
            name = get_product_name(new_product_url)
            self.links[name] = new_product_url
        update_config(self.__dict__)

    def load_config(self):
        try:
            config_object = open('config.json', 'r')
        except FileNotFoundError:
            print ("No config file found. Creating new config...")
            config_object = open('config.json', 'x')
            config_object.write(dumps(self.__dict__, indent=2))
            config_object.close()
        except Exception:
            print ("Error with loading configuration")
        finally:
            json_object = load(config_object)
            self.links = json_object("links")
            self.interval = json_object("interval")
            config_object.close()

    def update_config(self):
        new_file = open('config.json', 'w')
        json_object = dumps(self.__dict__, indent=2)
        new_file.write(json_object)
        new_file.close(


    def create_config():
        print(f"{Colour().default} Creating new config.json file.")
        new_file = open('config.json', 'x')
        new_file.close()
        print("New config.json file created. Type and enter 'help' for info on adding players and servers.")
