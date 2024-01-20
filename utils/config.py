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

    #loader for config.json file
    def config_fetcher(self):
        try:
            playerlist_file = open('./config.json', 'r')
            json_object = load(playerlist_file)
        except FileNotFoundError:
            logging.warning(f"{Colour().error} No config.json file found. {Colour().default}")
            create_config()
            self.initialize()
            return None
        except Exception:
            logging.error(f"{Colour().error} Error loading config.json file\nPlease fix any issues with config file before starting checker.{Colour().default}")
            self.__init__()
            return None
        else:
            playerlist_file.close()
            return json_object

    #loads config.json values / Initializes a config.json file if one is not found
    def load_config(self):
        json_object = self.config_fetcher()
        if (json_object == None):
            return
        if not (self.config_is_valid(json_object)):
            return
        self.players = json_object["players"]
        self.servers = json_object["servers"]
        self.interval = json_object["interval"]
        self.logger_on = bool(json_object["logger_on"])
        self.logall_on = bool(json_object["logall_on"])

    def update_config(self):
        new_file = open('config.json', 'w')
        json_object = dumps(self.__dict__, indent=2)
        new_file.write(json_object)
        new_file.close()


    def create_config():
        print(f"{Colour().default} Creating new config.json file.")
        new_file = open('config.json', 'x')
        new_file.close()
        print("New config.json file created. Type and enter 'help' for info on adding players and servers.")
