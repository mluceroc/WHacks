class Location: 
    def __init__(self, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
    
    def __str__(self):
        return self.latitude + " " + self.longitude
    
    def __hash__(self):
        return hash((self.latitude, self.longitude))

    def __eq__(self, other):
        return hash((self.latitude, self.longitude)) == hash((other.latitude, other.longitude))
    