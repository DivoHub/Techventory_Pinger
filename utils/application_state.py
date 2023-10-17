class ApplicationState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ApplicationState, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.continuing = False
        self.deal_list = []
        self.in_stock_dict = {}
        self.error_count = 0

    def toggle_continuing(self):
        if (self.continuing):
            self.continuing = False
        else:
            self.continuing = True

