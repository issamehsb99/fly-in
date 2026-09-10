
class hubs:
    def __init__(self):
        self.hubs = []
        self.cordinates = []
        self.color = []
        self.zone = []
        self.max_drones = []
        self.connection = []
        self.prev = None


class connection:
    def __init__(self):
        self.connection = []
        self.cordinates = []
        self.color = []
        self.zone = []
        self.visited = []
        self.prev = None


class algo:
    def find_path(self, start, end):
        visited = set()
        
